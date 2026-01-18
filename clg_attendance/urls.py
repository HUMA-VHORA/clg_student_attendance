from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def home(request):
    return HttpResponse("College Attendance System API Running")

urlpatterns = [
    path('', home),   # ✅ homepage

    path('admin/', admin.site.urls),

    # UI routes
    path('students/', include('students.urls')),
    path('attendance/', include('attendance.urls')),

    # API routes
    path('api/students/', include('students.urls')),
    path('api/attendance/', include('attendance.urls')),
]

