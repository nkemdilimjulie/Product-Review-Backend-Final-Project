from rest_framework import generics, pagination, permissions
from .permissions import IsAuthorOrReadOnly 
from rest_framework.permissions import IsAuthenticated
from .models import Marketer
from .serializers import MarketerSerializer
from rest_framework.viewsets import ModelViewSet
from django.core.exceptions import PermissionDenied


class MarketerPagination(pagination.PageNumberPagination):
    page_size = 10  # Adjust per your needs
    page_size_query_param = 'page_size'
    max_page_size = 100


# Create your views here.
class MarketerListView(generics.ListCreateAPIView):
    # permission_classes = [IsAuthenticated]
    permission_classes = [IsAuthorOrReadOnly]
    queryset = Marketer.objects.all()
    serializer_class = MarketerSerializer
    pagination_class = MarketerPagination
    
    
    # to create an entry in Marketer table by a logged in user who has an attribute 'is_marketer'
    def perform_create(self, serializer):
        if self.request.user.is_authenticated and self.request.user.is_marketer:
            serializer.save(author=self.request.user)
        else:
           raise PermissionDenied

class MarketerDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Marketer.objects.all()
    serializer_class = MarketerSerializer



class MarketerViewSet(ModelViewSet):
    serializer_class = MarketerSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Marketer.objects.filter(author=self.request.user)
