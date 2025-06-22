from rest_framework import serializers 
from .models import Job

class JopSerailizers(serializers.ModelSerializer):
    category=serializers.StringRelatedField()
    location=serializers.StringRelatedField()
    class Meta:
        model=Job
        fields='__all__'


class JobDetailSerializers(serializers.ModelSerializer):
    category=serializers.StringRelatedField()
    location=serializers.StringRelatedField()
    class Meta:
        model=Job
        fields='__all__'

