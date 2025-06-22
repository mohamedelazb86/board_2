from rest_framework import serializers
from .models import Post,Review



class ReviewSerailizers(serializers.ModelSerializer):
    post=serializers.StringRelatedField()
    class Meta:
        model=Review
        fields='__all__'

class PostSerializers(serializers.ModelSerializer):
    category=serializers.StringRelatedField()
    user=serializers.StringRelatedField()
    review=ReviewSerailizers(source='review_post',many=True)
    class Meta:
        model=Post
        fields='__all__'