from rest_framework import generics, permissions
#from .permissions import IsAuthorOrReadOnly 
from rest_framework.permissions import IsAuthenticated
from .models import Marketer
from .serializers import MarketerSerializer
from django.core.exceptions import PermissionDenied

# Create your views here.
class MarketerListView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Marketer.objects.all()
    serializer_class = MarketerSerializer
    
    
    # to create an entry in Marketer table by a logged in user who has an attribute 'is_marketer'
    def perform_create(self, serializer):
        #if self.request.user.is_authenticated and self.request.user.is_marketer:
        serializer.save(author=self.request.user)
        # else:
        #     raise PermissionDenied

class MarketerDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Marketer.objects.all()
    serializer_class = MarketerSerializer