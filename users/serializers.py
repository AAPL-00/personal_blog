from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth.password_validation import validate_password

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'email',]

class CreateUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only =True, allow_blank=True)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password']
        extra_kwargs = {
            'username': {'required': True, 'allow_blank': False},
            'email': {'required': True, 'allow_blank': False}
        }

    def validate_username(self, value):
        if CustomUser.objects.filter(user=value).exists():
            raise serializers.ValidationError("El nombre de usuario ya está en uso")
        return value
    
    def validate_email(self, value):
        if CustomUser.objects.filter(email=value).exists():
            raise serializers.ValidationError("El correo ya está en uso")
        return value
    
    def validate_password(self, value):
        validate_password(value, user=None)
        return value
    
    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            username = validated_data['username'],
            email = validated_data['email'],
            password = validated_data['password']
        )
        return user