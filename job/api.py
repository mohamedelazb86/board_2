from . import serializers
from rest_framework import generics
from .models import Job
from  .mypagination import MyPagination

class JobApi(generics.ListAPIView):
    queryset=Job.objects.all()
    serializer_class=serializers.JobDetailSerializers
    pagination_class=MyPagination

class JobDetailApi(generics.RetrieveAPIView):
    queryset=Job.objects.all()
    serializer_class=serializers.JobDetailSerializers


