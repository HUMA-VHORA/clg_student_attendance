from django.http import JsonResponse
from .models import Student
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
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
        return JsonResponse(data, safe=False)

    if request.method == 'POST':
        try:
            body = json.loads(request.body.decode('utf-8'))

            student = Student.objects.create(
                student_id=body.get('student_id'),
                name=body.get('name'),
                department=body.get('department')
            )

            return JsonResponse({'message': 'Student added successfully'})

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
