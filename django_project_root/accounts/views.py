from rest_framework import generics, permissions
from .models import CustomUser
from .serializers import CustomUserSerializer, CustomUserDetailsSerializer


class UserListView(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


class CustomUserDetailsView(generics.RetrieveAPIView):
    """
    Accepts GET method.

    Display fields: pk, username, email, first_name, last_name, user_type
    Read-only fields: pk, username, email, first_name, last_name, user_type

    Returns UserModel fields + additional computed field 'user_type'.
    """
    serializer_class = CustomUserDetailsSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self):
        return self.request.user
    