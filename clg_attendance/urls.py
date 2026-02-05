from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

from rest_framework_simplejwt.views import TokenRefreshView
from users.views import CustomTokenObtainPairView   


def home(request):
    return HttpResponse("College Attendance System API Running")


urlpatterns = [
    path('', home),

    path('admin/', admin.site.urls),

    # JWT Authentication (CUSTOM TOKEN VIEW)
    path('api/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Students APIs
    path('api/students/', include('students.urls')),

    # Attendance APIs
    path('api/attendance/', include('attendance.urls')),
]
