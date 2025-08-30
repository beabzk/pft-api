from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.permissions import AllowAny
from .serializers import UserSerializer

class UserRegistrationView(generics.CreateAPIView):
    """
    API view to create a new user.
    """
    queryset = User.objects.all()
    permission_classes = (AllowAny,) # Anyone can access this view to register
    serializer_class = UserSerializer