from rest_framework import serializers
from .models import Marketer


class MarketerSerializer(serializers.ModelSerializer):
    # excludes option to choose any author in Django web API
    # the author is currently logged user 
    author = serializers.PrimaryKeyRelatedField(read_only=True) 
    class Meta:
        model = Marketer
        fields = "__all__"