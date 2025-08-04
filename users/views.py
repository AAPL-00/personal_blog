from users.serializers import UserSerializer, CreateUserSerializer, PasswordUpdateSerializer
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated

class UserView(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user

class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = CreateUserSerializer

class PasswordUpdateView(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PasswordUpdateSerializer

    def get_object(self):
        return self.request.user
