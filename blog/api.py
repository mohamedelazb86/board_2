from .serializers import PostSerializers
from rest_framework import filters
from rest_framework import filters
from .mypagination import MyPagination

from django_filters.rest_framework import DjangoFilterBackend


from rest_framework import generics
from .models import Post

class PostApi(generics.ListAPIView):
    queryset=Post.objects.all()
    serializer_class=PostSerializers

    filter_backends = [filters.SearchFilter,DjangoFilterBackend,filters.OrderingFilter]
    search_fields = ['ttile', 'content']

    
    filterset_fields = ['category', 'draft']

   
    ordering_fields = ['title',]

    
    pagination_class=MyPagination

    