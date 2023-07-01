from django.urls import path, include
from core.views import CreateUser

urlpatterns = [
    path('user', CreateUser.as_view(), name="Create-user")
]
