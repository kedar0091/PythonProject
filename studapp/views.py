import json
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser

from studapp.models import Student,StudentInfo
from .serializer import StudentSerializer, StudentInfoSerializer

#############   STUDENT CRUD OPERATION  #################

class StudentsOperations(APIView):
    #GET ALL STUDENTS
    def get(self, request, format =None):
        try:
            getData = Student.objects.all()
            serializer = StudentSerializer(getData, many=True)
            return JsonResponse(serializer.data, safe=False)
        except Student.DoesNotExist:
            return JsonResponse("msg: Invalid", safe=False)

    #ADD STUDENT
    def post(self, request, format=None):
        try:
            jsonData = JSONParser().parse(request)
            print(jsonData)
            serializer = StudentSerializer(data=jsonData)
            print(serializer.is_valid())
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, safe=False)
            return JsonResponse("msg: Invalid", safe=False)
        except Exception as e:
            print(e)
            return JsonResponse("msg: Invalid", safe=False)

    #UPDATE STUDENT FROM ID
    def put(self, request, format = None):
        jsonData = JSONParser().parse(request)
        print(jsonData)
        try:
            getData = Student.objects.get(id=jsonData['id'])
            serializer = StudentSerializer(getData, jsonData)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse("User Updated", safe=False)
            return JsonResponse("Invalid request", safe=False)
        except Student.DoesNotExist:
           return JsonResponse("msg: ID NOT FOUND", safe=False)

    #DELETE STUDENT FROM ID
    def delete(self, request, format = None):
        jsonData = JSONParser().parse(request)
        print(jsonData)
        try:
            getData = Student.objects.get(id=jsonData['id']) 
            getData.delete()
            return JsonResponse("User Deleted", safe=False)
        except Student.DoesNotExist:
            return JsonResponse("msg: ID NOT FOUND", safe=False)


class GetStudent(APIView):
    # GET SINGLE STUDENT FROM ID
    def get(self, request, format =None):
        jsonData = JSONParser().parse(request)
        print(jsonData['id'])
        try:
            getData = Student.objects.get(id=jsonData['id'])
            print(getData)
            serializer = StudentSerializer(getData)
            return JsonResponse(serializer.data, safe=False)
        except Student.DoesNotExist:
            return JsonResponse("msg: Invalid", safe=False)

