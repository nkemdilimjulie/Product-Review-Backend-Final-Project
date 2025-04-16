from rest_framework import serializers
from .models import Marketer


# class MarketerSerializer(serializers.ModelSerializer):
#     # excludes option to choose any author in Django web API
#     # the author is currently logged user 
#     author = serializers.PrimaryKeyRelatedField(read_only=True) 
#     class Meta:
#         model = Marketer
#         fields = "__all__"

class MarketerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marketer
        fields = '__all__'
        read_only_fields = ['author']  # <- Important

    def create(self, validated_data):
        validated_data['author'] = self.context['request'].user
        return super().create(validated_data)
