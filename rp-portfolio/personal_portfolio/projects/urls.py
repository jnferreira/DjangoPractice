from django.urls import path

from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [

    path("", views.project_index, name="project_index"),

    path("<int:pk>/", views.project_detail, name="project_detail"),

    path("add/", views.add_projects, name="add_projects"),

    path("auth/", views.auth, name="auth"),

    path("logout/", views.logout_view, name="logout_view"),

    path('auth/', auth_views.LoginView.as_view()),
]