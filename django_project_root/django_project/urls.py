"""
URL configuration for django_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from drf_yasg.views import get_schema_view
from drf_yasg import openapi
# Swagger related imports of urls and views
from rest_framework.permissions import IsAdminUser
from dj_rest_auth.registration.views import RegisterView
from dj_rest_auth.views import LoginView, LogoutView
from mobiles.urls import urlpatterns as mobiles_urls
from reviews.urls import urlpatterns as reviews_urls
from marketers.urls import urlpatterns as marketers_urls


# Setup schema view for Swagger. Only logged in admin user has access.
schema_view = get_schema_view(
    openapi.Info(
        title="Reviewer project API",
        default_version='v1',
        description="API documentation for Reviewer project",
        #terms_of_service="https://www.yourapi.com/terms/",
    ),
    public=False,
    permission_classes=(IsAdminUser,),
    # selected patterns and views for Swagger only
    patterns=mobiles_urls + reviews_urls + marketers_urls +
        [path('users/registration/', RegisterView.as_view(), name='rest_register'),
         path('users/login/', LoginView.as_view(), name='rest_login'),
         path('users/logout/', LogoutView.as_view(), name='rest_logout')
         ]
)

# Project urls
urlpatterns = [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path("admin/", admin.site.urls),
    path("api/", include("accounts.urls")),
    path("api/", include("mobiles.urls")),
    path("api/", include("reviews.urls")),
    path("api/", include("marketers.urls")),
    path('api/', include('contacts.urls')), 
]
