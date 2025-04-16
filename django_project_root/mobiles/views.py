# from rest_framework import generics, permissions # permissions-
# from .models import Mobiles
# from .serializers import MobilesSerializer


# class MobileListView(generics.ListCreateAPIView):
#     permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
#     queryset = Mobiles.objects.all()
#     serializer_class = MobilesSerializer


# class MobileDetailView(generics.RetrieveUpdateDestroyAPIView):
#     permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
#     queryset = Mobiles.objects.all()
#     serializer_class = MobilesSerializer


from rest_framework import viewsets
from .models import Mobiles
from .serializers import MobilesSerializer

class MobilesViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Mobiles.objects.all()
    serializer_class = MobilesSerializer
