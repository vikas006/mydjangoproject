from django.urls import path
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
    path("~redirect/", view=user_redirect_view, name="redirect"),
    path("~update/", view=user_update_view, name="update"),
    path("<str:username>/", view=user_detail_view, name="detail"),
]
