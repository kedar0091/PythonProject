from django.shortcuts import render
import email
import json
import requests
from django.http import Http404, JsonResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.contrib.auth.models import User
from .models import UserProfile
from django.utils.crypto import get_random_string

from django.db.models import Q
from rest_framework.authtoken.models import Token

# Create your views here.
class UserDetail(APIView):
    def post(self, request, format=None):
        body = request.body
        json_data = json.loads(body.decode("utf-8"))

        password = json_data["password"]
        email = json_data["email"]

        if password == "":
            return ("password cannot be empty")
        if email == "":
            return ("email cannot be empty")

        # check if that email already exists
        user = None
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return (f"No such with email {email} exist")

        token_obj, __ = Token.objects.get_or_create(user=user)
        if user.is_active == 0:
            return "This user is inactive."

        if user.check_password(password):
            pass
        else:
            return ("Invalid Password")

        return JsonResponse(
            {
                "token": str(token_obj),
                "user_id": user.pk,
                "username": user.username,
                "first_name": user.first_name,
                "last_name": user.last_name,
            }
        )

class NewUser(APIView):
    def post(self, request, format=None):
        body = request.body
        json_data = json.loads(body.decode("utf-8"))

        first_name = json_data["first_name"]
        last_name = json_data["last_name"]
        password = json_data["password"]
        email = json_data["email"]
        mobile = json_data["mobile"]
       
        
        # validations
        if first_name == "":
            return JsonResponse("first_name cannot be empty",safe=False)

        if last_name == "":
            return JsonResponse("last_name cannot be empty",safe=False)
        if password == "":
            return JsonResponse("password cannot be empty",safe=False)
        if email == "":
            return JsonResponse("email cannot be empty",safe=False)
      
        try:
            user = User.objects.get(email=email.lower())
            return JsonResponse("User with such email already exists", safe=False)
        except User.DoesNotExist:
            pass

                         
        # all validated
        user = User.objects.create_user(
            username=get_random_string(length=10),
            email=email,
            first_name=first_name,
            last_name=last_name,
            password=password,
        )

        # add mobile to profile
        profile = UserProfile()
        profile.user = user
        profile.user_mobile = mobile if mobile != "" else " "
        profile.save()

        return JsonResponse(
            {
                "user_id": user.pk,
                "username": user.username,
                "first_name": user.first_name,
                "last_name": user.last_name,
                "email":user.email,
                "mobile": profile.user_mobile,
            }
        )