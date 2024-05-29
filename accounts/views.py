from django.shortcuts import render
from rest_framework import permissions, viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from .models import *
from .serializers import *

# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User
#     serializer_class = UserSerializer
    
    # def list(self, request, *args, **kwargs):
    #     queryset = self.filter_queryset(self.get_queryset().order_by('email'))

    #     page = self.paginate_queryset(queryset)
    #     if page is not None:
    #         serializer = self.get_serializer(page, many=True)
    #         return self.get_paginated_response(serializer.data)

    #     serializer = self.get_serializer(queryset, many=True)
    #     return Response(serializer.data)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def user_name(request):
    return Response({"email": request.user.email})


    