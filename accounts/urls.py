from django.urls import path
from .views import RegisterView, ProtectedProfileView

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
urlpatterns = [
    path('register/',RegisterView.as_view(), name='register-accounts'),
    path('login/', TokenObtainPairView.as_view(), name='login-accounts'),
    path('refresh/', TokenRefreshView.as_view(), name='refresh-accounts'),
     # Test protected route
    path('profile/', ProtectedProfileView.as_view(), name='user_profile'),
]
