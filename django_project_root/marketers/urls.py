from django.urls import path
from .views import MarketerListView, MarketerDetailView

urlpatterns = [
    path("marketers/", MarketerListView.as_view(), name="marketer-list"),
    path("marketers/<int:pk>/", MarketerDetailView.as_view(), name="marketer-detail"),
]