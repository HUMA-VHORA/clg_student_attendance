from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.core.cache import cache
from .models import Student

def is_teacher(user):
    return user.groups.filter(name='Teacher').exists()

def is_student(user):
    return user.groups.filter(name='Student').exists()


@method_decorator(cache_page(60*5), name='dispatch')
class StudentListAPI(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        if not is_teacher(request.user):
            return Response({'error': 'Access denied'}, status=403)

        students = Student.objects.all()
        data = [{
            'id': s.id,
            'student_id': s.student_id,
            'name': s.name,
            'department': s.department
        } for s in students]
        return Response(data)

    def post(self, request):
        if not is_teacher(request.user):
            return Response({'error': 'Access denied'}, status=403)

        body = request.data
        try:
            student = Student.objects.create(
                student_id=body['student_id'],
                name=body['name'],
                department=body['department']
            )
            cache.clear()
            return Response({'message': 'Student added successfully', 'id': student.id}, status=201)
        except Exception as e:
            return Response({'error': str(e)}, status=400)


@method_decorator(cache_page(60*5), name='dispatch')
class MyStudentInfoAPI(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, student_id):
        if not is_student(request.user):
            return Response({'error': 'Access denied'}, status=403)

        if request.user.student.id != student_id:
            return Response({'error': 'Access denied'}, status=403)

        try:
            s = Student.objects.get(id=student_id)
            data = {
                'id': s.id,
                'student_id': s.student_id,
                'name': s.name,
                'department': s.department
            }
            return Response(data)
        except Student.DoesNotExist:
            return Response({'error': 'Student not found'}, status=404)
