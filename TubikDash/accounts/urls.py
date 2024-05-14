from django.contrib.auth import views
from django.urls import path

import accounts.forms
import accounts.views

app_name = "accounts"

urlpatterns = [
    path('register/', accounts.views.register, name='register'),
]
