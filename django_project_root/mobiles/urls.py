from django.urls import path
from .views import MobileListView, MobileDetailView

urlpatterns = [
    path("mobiles/", MobileListView.as_view(), name="mobile-list"),
    path("mobiles/<str:pk>/", MobileDetailView.as_view(), name="mobile-detail"),
]
