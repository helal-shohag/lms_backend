from django.urls import path
from .views import user_list
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
urlpatterns = [
    path('', user_list, name='user_list'),
    path('token/',TokenObtainPairView.as_view,name='token'),
]