from django.urls import path
from .views import AttendanceAPI, AttendanceByDateAPI, AttendanceByStudentAPI

urlpatterns = [
    path('', AttendanceAPI.as_view(), name='attendance_api'),
    path('by-date/<str:date>/', AttendanceByDateAPI.as_view(), name='attendance_by_date'),
    path('by-student/<int:student_id>/', AttendanceByStudentAPI.as_view(), name='attendance_by_student'),
]

