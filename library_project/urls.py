from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),

    # URL for obtaining a new JWT access and refresh token pair.
    # Used for user authentication.
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),

    # URL for refreshing the JWT access token.
    # This is useful when the access token has expired but the refresh token is still valid.
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # URL pattern for all API endpoints defined in the library_app.
    # This includes the app's URL configurations for API routes.
    path('api/library/', include('library_app.urls')),
]
