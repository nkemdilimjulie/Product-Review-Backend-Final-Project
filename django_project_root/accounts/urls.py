# from django.urls import path
# from .views import UserListView, UserDetailView

# urlpatterns = [
#     path("users/", UserListView.as_view(), name="user-list"),
#     path("users/<int:pk>/", UserDetailView.as_view(), name="user-detail"),
# ]

# mmmmmmmmmmmmmmmmm authentication endpoints for login, logout, and registration. mmmmmmmmmmm
from django.urls import path, include
from .views import CustomUserDetailsView

urlpatterns = [
    path("users/", include("dj_rest_auth.urls")),  # Login, Logout, Password Reset
    path("users/registration/", include("dj_rest_auth.registration.urls")),  # Registration
    path("users/user_details/", CustomUserDetailsView.as_view()), # Type of logged in user
]
