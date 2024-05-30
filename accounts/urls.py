from django.contrib import admin
from django.urls import path, include

from rest_framework.routers import DefaultRouter
from .views import *

# router = DefaultRouter()
# router.register(r'user-view', UserViewSet)


urlpatterns = [
    path('', include('dj_rest_auth.urls')),
    path('', include('dj_rest_auth.registration.urls')),
    path('user-name/', user_name),
    #path('', include(router.urls)),
]