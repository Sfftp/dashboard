from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from TubikDash import views
from django.contrib.auth import views as login_view

urlpatterns = [
    path("admin/", admin.site.urls),
    path("about/", include("about.urls", namespace="about")),
    path("main/", include("homepage.urls", namespace="homepage")),
    path("dashes/", include("dashes.urls")),
    path('django_plotly_dash/', include('django_plotly_dash.urls')),
    path('accounts/login/', login_view.LoginView.as_view(template_name="accounts/login.html"), name="login"),
    path('accounts/logout/', login_view.LogoutView.as_view(next_page="/"), name="logout"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls')),
    path("", views.redirect_to_homepage),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [path("__debug__/", include(debug_toolbar.urls)),] + urlpatterns
