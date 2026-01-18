from django.urls import path
from . import views

urlpatterns = [
    path('', views.attendance_api, name='attendance_api'),  # GET + POST
    path('by-date/<str:date>/', views.attendance_by_date),
    path('by-student/<int:student_id>/', views.attendance_by_student),
]
