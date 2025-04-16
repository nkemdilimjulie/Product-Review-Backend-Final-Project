# from django.urls import path
# from .views import MobileListView, MobileDetailView

# urlpatterns = [
#     path("mobiles/", MobileListView.as_view(), name="mobile-list"),
#     path("mobiles/<str:pk>/", MobileDetailView.as_view(), name="mobile-detail"),
# ]



from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MobilesViewSet

router = DefaultRouter()
router.register(r'mobiles', MobilesViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
