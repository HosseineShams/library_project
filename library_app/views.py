from rest_framework import viewsets, status, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Book, Author
from .serializers import BookSerializer, AuthorSerializer, UserSerializer
from rest_framework.permissions import AllowAny

class RegisterUserAPIView(APIView):
    """
    API view for registering new users. Open to all users without authentication.
    """
    permission_classes = [AllowAny]

    def post(self, request):
        """
        Handle POST request to create a new user. On successful creation,
        returns JWT tokens (refresh and access) for the user.
        """
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BookViewSet(viewsets.ModelViewSet):
    """
    ViewSet for handling CRUD operations for the Book model.
    Includes filters for publication date and availability status, and search by title.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['publication_date', 'availability_status']
    search_fields = ['title']

    def perform_create(self, serializer):
        """
        Overridden method to set the 'user' field to the current user on creation of a new book.
        """
        serializer.save(user=self.request.user)

class AuthorViewSet(viewsets.ModelViewSet):
    """
    ViewSet for handling CRUD operations for the Author model.
    Includes search functionality by name and bio.
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'bio']
