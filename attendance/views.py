from django.http import JsonResponse
from .models import Attendance
from students.models import Student
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def attendance_list(request):
    if request.method == 'GET':
        records = Attendance.objects.all()
        data = []
        for r in records:
            data.append({
                'id': r.id,
                'student_id': r.student.student_id,
                'name': r.student.name,
                'date': r.date,
                'status': r.status
            })
        return JsonResponse(data, safe=False)

    if request.method == 'POST':
        body = json.loads(request.body)
        student = Student.objects.get(id=body['student_id'])
        Attendance.objects.create(
            student=student,
            date=body['date'],
            status=body['status']
        )
        return JsonResponse({'message': 'Attendance marked'})
def attendance_by_date(request, date):
    records = Attendance.objects.filter(date=date)
    data = []
    for r in records:
        data.append({
            'student_id': r.student.student_id,
            'name': r.student.name,
            'status': r.status
        })
    return JsonResponse(data, safe=False)


def attendance_by_student(request, student_id):
    records = Attendance.objects.filter(student__id=student_id)
    data = []
    for r in records:
        data.append({
            'date': r.date,
            'status': r.status
        })
    return JsonResponse(data, safe=False)
