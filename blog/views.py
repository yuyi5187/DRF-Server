from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Post
from .serializers import PostSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset().order_by('-updated_at'))

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)