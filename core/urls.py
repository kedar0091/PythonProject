from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path("login/", views.UserDetail.as_view()),
    # path("roles/", views.RolesMeta.as_view()),
    path("register/", views.NewUser.as_view()),
    # path("updateuser/", views.NewUser.as_view()),
    # path("userlisting/", views.UserListing.as_view()),
    # path("getuser/<int:user_id>/", views.ExistingUser.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
