from django.urls import path, include
from rest_framework.routers import DefaultRouter

from myproject.users.api.views import UserViewSet
from myproject.users.views import (
    user_detail_view,
    user_redirect_view,
    user_update_view)

app_name = "users"
router = DefaultRouter()
router.register('users', UserViewSet)
urlpatterns = [
    path('', include(router.urls)),
]
