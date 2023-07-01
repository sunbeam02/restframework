from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from django.contrib.auth.models import User
from core.serializer import UserSerializer

# Create your views here.

class CreateUser(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
