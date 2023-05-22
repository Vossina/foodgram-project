from rest_framework import routers
from django.urls import path, include
from .views import UserViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
  path('api/', include(router.urls)),
  path('v1/', include('djoser.urls.jwt')),
]