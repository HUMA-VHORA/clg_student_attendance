from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.core.cache import cache

from .models import Attendance
from students.models import Student
from .decorators import role_required   # ✅ NEW


@method_decorator(cache_page(60*5), name='dispatch')
class AttendanceAPI(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    @role_required(['Teacher'])
    def get(self, request):
        records = Attendance.objects.select_related('student').all()
        data = [{
            'id': a.id,
            'date': str(a.date),
            'status': a.status,
            'student_id': a.student.id,
            'name': a.student.name
        } for a in records]
        return Response(data)

    @role_required(['Teacher'])
    def post(self, request):
        body = request.data
        try:
            student = Student.objects.get(id=body['student_id'])
            Attendance.objects.update_or_create(
                student=student,
                date=body['date'],
                defaults={'status': body['status']}
            )
            cache.clear()
            return Response({'message': 'Attendance saved'}, status=201)

        except Student.DoesNotExist:
            return Response({'error': 'Student not found'}, status=404)
        except Exception as e:
            return Response({'error': str(e)}, status=400)


@method_decorator(cache_page(60*5), name='dispatch')
class AttendanceByDateAPI(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    @role_required(['Teacher'])
    def get(self, request, date):
        records = Attendance.objects.select_related('student').filter(date=date)
        data = [{
            'id': a.id,
            'date': str(a.date),
            'status': a.status,
            'student_id': a.student.id,
            'name': a.student.name
        } for a in records]
        return Response(data)


@method_decorator(cache_page(60*5), name='dispatch')
class AttendanceByStudentAPI(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    @role_required(['Student'])
    def get(self, request, student_id):

        # Extra safety check (student can see only own data)
        if request.user.student.id != student_id:
            return Response({'error': 'Access denied'}, status=403)

        records = Attendance.objects.select_related('student').filter(student__id=student_id)
        data = [{
            'id': a.id,
            'date': str(a.date),
            'status': a.status,
            'student_id': a.student.id,
            'name': a.student.name
        } for a in records]
        return Response(data)
