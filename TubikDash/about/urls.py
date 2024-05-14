from django.contrib.auth import views
from django.urls import path

from about import views

app_name = "about"

urlpatterns = [
    path("", views.main_page, name="main_page")
]