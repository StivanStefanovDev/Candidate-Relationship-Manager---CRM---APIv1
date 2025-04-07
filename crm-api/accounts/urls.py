from django.urls import path
from .views import RegisterView, MeView


# POST    /api/auth/register/           # Register a new user
# POST    /api/auth/token/              # Log in and get JWT access + refresh tokens
# POST    /api/auth/token/refresh/      # Refresh access token using refresh token
# GET     /api/auth/me/                 # Get current logged-in user info


urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("me/", MeView.as_view(), name="me"),
]
