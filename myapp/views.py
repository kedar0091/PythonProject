from rest_framework.authtoken.models import Token
from django.contrib.auth.hashers import make_password
from django.shortcuts import render
from django.http import JsonResponse
from .models import Employee
from .serializers import EmployeeSerializer, UserSerializer
from django.contrib.auth.models import User

from rest_framework.views import APIView
import json
from rest_framework.parsers import JSONParser

# Create your views here.

# Get All Employee List


class EmployeeListView(APIView):
    def get(self, request, format=None):
        try:
            event = Employee.objects.all()
            serializer = EmployeeSerializer(event, many=True)
            return JsonResponse(serializer.data, safe=False)
        except Exception:
            return JsonResponse("msg: Invalid", safe=False)


# Get single Employee by Id
class GetEmployeeByID(APIView):
    def get(self, request, pk):
        try:
            emp = Employee.objects.get(pk=pk)
            serializer = EmployeeSerializer(emp)
            return JsonResponse(serializer.data, safe=False)
        except Exception:
            return JsonResponse("msg: Invalid", safe=False)


# Get Django User List
class UserListView(APIView):
    def get(self, request, format=None):
        try:
            userList = User.objects.all()
            serializer = UserSerializer(userList, many=True)
            return JsonResponse(serializer.data, safe=False)
        except Exception:
            return JsonResponse("msg: Invalid", safe=False)

# Add Employee 1
# class AddEmployeeView(APIView):
#     def post(self, request):
#         try:
#             serializer = EmployeeSerializer(data=request.data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return JsonResponse(serializer.data, safe=False)
#             return JsonResponse("msg: Invalid", safe=False)
#         except Exception as e:
#             print(e)
#             return JsonResponse("msg: Invalid", safe=False)


# Add Employee way 2

class AddEmployeeView(APIView):
    def post(self, request):
        try:
            jsonData = JSONParser().parse(request)
            serializer = EmployeeSerializer(data=jsonData)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, safe=False)
            return JsonResponse("msg: Invalid", safe=False)
        except Exception as e:
            print(e)
            return JsonResponse("msg: Invalid", safe=False)

# Delete employee by Id


class DeleteEmpView(APIView):
    def delete(self, request, pk):
        try:
            emp = Employee.objects.get(pk=pk)
            emp.delete()
            return JsonResponse("User Deleted", safe=False)
        except Exception as e:
            print(e)
            return JsonResponse("msg: Invalid", safe=False)

# Delete multiple


# class DeleteMultiEmpView(APIView):
#     def delete(self, request, pk):
#         try:
#             emp = Employee.objects.get(pk=pk)
#             emp.delete()
#             return JsonResponse("User Deleted", safe=False)
#         except Exception as e:
#             print(e)
#             return JsonResponse("msg: Invalid", safe=False)


# Update Employee by Id

class UpdateEmpView(APIView):
    def put(self, request, pk):
        try:
            empData = Employee.objects.get(pk=pk)
            serializer = EmployeeSerializer(empData, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse("User Updated", safe=False)
            return JsonResponse("Invalid request", safe=False)
        except Exception as e:
            return JsonResponse("msg : Invalid request", safe=False)


# Registration And Login Functionality with User


class RegisterEmployeeView(APIView):
    def post(self, request, instance=None):
        try:
            serializer = UserSerializer(data=request.data)
            if serializer.is_valid():
                # if User.objects.filter(email=request.data['email']).exists():
                #     return JsonResponse("User already exist", safe=False)
                # else:
                #     serializer.save(password=make_password(
                #         request.data['password']))

                user = Employee.objects.get(email=request.data['email'])
                token, created = Token.objects.create(user=user)
                print(token.key)
                #token, created = Token.objects.get_or_create(user=emp)
                token_dict = {'token': token.key, 'data': serializer.data}
                return JsonResponse(token_dict, safe=False)
            return JsonResponse("msg: Invalid", safe=False)
        except Exception as e:
            print(e)
            return JsonResponse("msg: Invalid Request", safe=False)
