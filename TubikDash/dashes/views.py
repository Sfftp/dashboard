from django.shortcuts import render

# Create your views here.
import matplotlib.pyplot as plt
from io import BytesIO
import base64
from django.http import HttpResponse
from .currency_exchange_rate import hui


def dash_demo_one(request):
    return render(request, "dashes/dash1.html")


def exchange_info(request):
    n = []
    result = hui()
    for i in result:
        element1, element2 = result[i]["Name"], result[i]["VunitRate"]
        n.append([element1, element2])
    context_dict = {"n": n}
    return render(request, "dashes/exchange_info.html", context=context_dict)


def main(request):
    return render(request, "dashes/catalog.html")
