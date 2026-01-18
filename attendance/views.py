from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Attendance
from students.models import Student
import json
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import StudentSerializer



@csrf_exempt
def attendance_api(request):

    if request.method == 'GET':
        records = Attendance.objects.select_related('student').all()
        data = []
        for a in records:
            data.append({
                'id': a.id,
                'date': str(a.date),
                'status': a.status,
                'student_id': a.student.id,
                'name': a.student.name
            })
        return JsonResponse(data, safe=False)

    elif request.method == 'POST':
        try:
            body = json.loads(request.body)
            student = Student.objects.get(id=body['student_id'])

            Attendance.objects.update_or_create(
                student=student,
                date=body['date'],
                defaults={'status': body['status']}
            )

            return JsonResponse({'message': 'Attendance saved'}, status=201)

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
def attendance_by_date(request, date):
    records = Attendance.objects.select_related('student').filter(date=date)
    data = [{
        'id': a.id,
        'date': str(a.date),
        'status': a.status,
        'student_id': a.student.id,
        'name': a.student.name
    } for a in records]
    return JsonResponse(data, safe=False)


def attendance_by_student(request, student_id):
    records = Attendance.objects.select_related('student').filter(student__id=student_id)
    data = [{
        'id': a.id,
        'date': str(a.date),
        'status': a.status,
        'student_id': a.student.id,
        'name': a.student.name
    } for a in records]
    return JsonResponse(data, safe=False)

