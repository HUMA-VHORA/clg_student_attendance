from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.cache import cache_page
from django.core.cache import cache

from .models import Student
import json


@csrf_exempt
@cache_page(60 * 5)   
def student_list(request):

    if request.method == 'GET':
        students = Student.objects.all()
        data = []

        for s in students:
            data.append({
                'id': s.id,
                'student_id': s.student_id,
                'name': s.name,
                'department': s.department
            })

        return JsonResponse(data, safe=False, status=200)

    elif request.method == 'POST':
        try:
            body = json.loads(request.body)

            student = Student.objects.create(
                student_id=body['student_id'],
                name=body['name'],
                department=body['department']
            )

            cache.clear()   

            return JsonResponse(
                {'message': 'Student added successfully', 'id': student.id},
                status=201
            )

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
