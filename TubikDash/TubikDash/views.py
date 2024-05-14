from django.shortcuts import redirect


def redirect_to_homepage(request):
    return redirect("homepage:main")