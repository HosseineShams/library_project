from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Book, Author

class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for the User model. Handles serialization and deserialization
    for user creation, focusing on the username and password fields.
    """
    class Meta:
        model = User
        fields = ['username', 'password']
        extra_kwargs = {'password': {'write_only': True}}  # Ensures password is write-only for security

    def create(self, validated_data):
        """
        Overridden create method to handle user creation with hashed password.
        """
        user = User.objects.create_user(**validated_data)
        return user

class AuthorSerializer(serializers.ModelSerializer):
    """
    Serializer for the Author model. Handles all fields of the Author model
    for serialization and deserialization.
    """
    class Meta:
        model = Author
        fields = '__all__'  # Includes all fields from the Author model

class BookSerializer(serializers.ModelSerializer):
    """
    Serializer for the Book model. Handles all fields of the Book model
    for serialization and deserialization.
    """
    class Meta:
        model = Book
        fields = '__all__'  # Includes all fields from the Book model
