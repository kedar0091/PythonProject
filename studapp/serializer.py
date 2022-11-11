
from rest_framework import serializers
from .models import Student,StudentInfo

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = [
            "id",
            "name",
            "roll",
            "phone",
        ]


class StudentInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentInfo
        fields = [
            "state",
            "city",
        ]
    
