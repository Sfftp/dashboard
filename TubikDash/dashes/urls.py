from dashes import views
from django.urls import path
from dashes import stocks
from dashes.views import dash_demo_one, exchange_info, main

app_name = "dashes"

urlpatterns = [
    path("stocks/", dash_demo_one, name="dash_demo_one"),
    path("exchange_info/", exchange_info, name="exchange_info"),
    path("", main, name="dash_main"),
]


