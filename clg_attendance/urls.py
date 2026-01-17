from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def home(request):
    return HttpResponse("College Attendance System API Running")

urlpatterns = [
    path('', home),
    path('admin/', admin.site.urls),
    path('api/students/', include('students.urls')),
    path('api/attendance/', include('attendance.urls')),
]
