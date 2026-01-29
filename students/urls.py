from django.urls import path
from .views import StudentListAPI, MyStudentInfoAPI

urlpatterns = [
    path('', StudentListAPI.as_view(), name='student_list_api'),
    path('<int:student_id>/', MyStudentInfoAPI.as_view(), name='my_student_info_api'),
]
