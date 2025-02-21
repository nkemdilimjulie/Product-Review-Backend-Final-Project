from rest_framework import serializers
from .models import Mobiles


class MobilesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mobiles
        fields = "__all__"
