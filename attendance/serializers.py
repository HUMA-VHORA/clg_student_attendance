from rest_framework import serializers
from .models import Attendance
from students.serializers import StudentSerializer


class AttendanceSerializer(serializers.ModelSerializer):
    student_details = StudentSerializer(source='student', read_only=True)

    class Meta:
        model = Attendance
        fields = '__all__'
