from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path("employee_list/", views.EmployeeListView.as_view()),
    path("employee_details/<int:pk>", views.GetEmployeeByID.as_view()),
    path("employee_add/", views.AddEmployeeView.as_view()),
    path("employee_delete/<int:pk>", views.DeleteEmpView.as_view()),
    path("employee_update/<int:pk>", views.UpdateEmpView.as_view()),
    path("employee_user/", views.UserListView.as_view()),
    path("employee_register/", views.RegisterEmployeeView.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)
