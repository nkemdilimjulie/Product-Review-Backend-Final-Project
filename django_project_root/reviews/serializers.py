# from rest_framework import serializers
# from .models import Reviews


# class ReviewSerializer(serializers.ModelSerializer):
#     # exclude field to choose author in Django web API
#     author = serializers.PrimaryKeyRelatedField(read_only=True) 
#     class Meta:
#         model = Reviews
#         fields = "__all__"

from rest_framework import serializers
from .models import Reviews

class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Reviews
        fields = '__all__'

    def validate(self, data):
        request = self.context.get('request')
        if request and Reviews.objects.filter(author=request.user, phone=data['phone']).exists():
            raise serializers.ValidationError("You already reviewed this phone.")
        return data

