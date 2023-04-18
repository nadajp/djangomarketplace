from django.urls import path, include
from rest_framework_simplejwt.views import TokenRefreshView
from django.contrib.auth.views import LoginView, LogoutView

from .views import CustomUserCreateView, CustomTokenObtainPairView

urlpatterns = [
    path('login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup/', CustomUserCreateView.as_view(), name='signup'),
    path('api/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
