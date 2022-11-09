from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path("add_student/", views.StudentsOperations.as_view()),
    path("get_student_info/", views.StudentsOperations.as_view()),
    path("get_student/", views.StudentsOperations.as_view()),
    path("update_student/", views.StudentsOperations.as_view()),
    path("delete_student/", views.StudentsOperations.as_view()),
    # path("script/", views.rscript.as_view()),
   
]

urlpatterns = format_suffix_patterns(urlpatterns)
