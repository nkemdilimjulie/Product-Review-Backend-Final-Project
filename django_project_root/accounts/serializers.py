from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth import get_user_model

from dj_rest_auth.registration.serializers import RegisterSerializer

from dj_rest_auth.serializers import api_settings


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

# custom serializer expanding USER_DETAILS_SERIALIZER with extra field 'user_type' of: admin, visitor, marketer   
BaseUserSerializer = api_settings.USER_DETAILS_SERIALIZER
    
class CustomUserDetailsSerializer(BaseUserSerializer):
    user_type = serializers.SerializerMethodField()

    class Meta(BaseUserSerializer.Meta):
        fields = BaseUserSerializer.Meta.fields + ("user_type",)

    def get_user_type(self, user):
        if user.is_superuser:
            return 'admin'
        elif user.is_marketer:
            return 'marketer'
        else:
            return 'visitor'