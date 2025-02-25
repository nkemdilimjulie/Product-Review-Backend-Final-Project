from rest_framework import serializers
from .models import Reviews


class ReviewSerializer(serializers.ModelSerializer):
    # exclude field to choose author in Django web API
    author = serializers.PrimaryKeyRelatedField(read_only=True) 
    class Meta:
        model = Reviews
        fields = "__all__"
