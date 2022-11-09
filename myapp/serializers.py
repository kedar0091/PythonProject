from .models import Employee
from rest_framework import serializers
from django.contrib.auth.models import User
# class EmployeeSerializer(serializers.Serializer):
#     name = serializers.CharField(max_length=30)
#     email = serializers.EmailField()
#     password = serializers.CharField(max_length=30)
#     phone = serializers.CharField(max_length=10)

#     # class Meta:
#     #     model = Employee
#     #     fields = '__all__'


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'
        # fields = ['name', 'email', 'password', 'phone']

        def validate_email(self, value):
            if User.objects.filter(email=value).exists():
                raise serializers.ValidationError(
                    "This email already exists!.")
            return value


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email']
