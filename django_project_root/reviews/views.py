from rest_framework import generics, permissions
from .permissions import IsAuthorOrReadOnly 
from .models import Reviews
from .serializers import ReviewSerializer
from django.core.exceptions import PermissionDenied

class ReviewListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Reviews.objects.all()
    serializer_class = ReviewSerializer
    
    
    # to create reviews (by currently logged-in user only, excluding marketer users)
    def perform_create(self, serializer):
        if self.request.user.is_authenticated and self.request.user.is_marketer == False:
            serializer.save(author=self.request.user)
        else:
            raise PermissionDenied

        
class ReviewDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Reviews.objects.all()
    serializer_class = ReviewSerializer

    