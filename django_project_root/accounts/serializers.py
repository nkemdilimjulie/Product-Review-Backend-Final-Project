from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth import get_user_model

from dj_rest_auth.registration.serializers import RegisterSerializer

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["id", "username", "email"] #removed 'name' field


# custom register serializer based on RegisterSerializer + added checkbox field
class CustomRegisterSerializer(RegisterSerializer):
    # new checkbox field 'Is marketer'
    email = None # hide email field
    is_marketer = serializers.BooleanField(
        required=False,
        help_text=' *Use this option only to create a marketer account for advertisement purposes.')
     
    class Meta:
        model = get_user_model()
        fields = ["username", "password1", "password2", "is_marketer"]
    
    def save(self, request):
        user = super().save(request) # 1st parent's save() creates default user instance 
        user.is_marketer = self.validated_data.get('is_marketer', False)
        user.save() # 2nd save() updates existing user instance with additional attribute
        return user