from rest_framework import generics
from .models import Mobiles
from .serializers import MobilesSerializer


class MobileListView(generics.ListCreateAPIView):
    queryset = Mobiles.objects.all()
    serializer_class = MobilesSerializer


class MobileDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Mobiles.objects.all()
    serializer_class = MobilesSerializer
