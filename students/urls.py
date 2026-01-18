from django.urls import path
from . import views

urlpatterns = [
    path('', views.student_list, name='student_list_api'),   # API + UI JSON
]

