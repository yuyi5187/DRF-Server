from django.contrib import admin
from django.urls import path, include

from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'post', PostViewSet)

urlpatterns = [
    #path('', PostViewSet.as_view({'get':'list', 'post':'create'})),
    path("", include(router.urls)),
]
