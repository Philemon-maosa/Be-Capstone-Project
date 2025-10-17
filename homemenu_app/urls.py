from django.contrib import admin
from django.urls import path, include
from .views import home_view
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from users.views import RegisterView, login_view  # include our standalone login_view

urlpatterns = [
    path('', home_view, name='home'),
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    #  Authentication routes (standalone, no JWT required)
    path('api/auth/register/', RegisterView.as_view(), name='register'),
    path('api/auth/login/', login_view, name='login'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    #  Other app routes
    path('api/users/', include('users.urls')),
    path('api/', include('recipes.urls')),
    path('api/pantry/', include('pantry.urls')),
    path('api/kitchenlist/', include('kitchenlist.urls')),
]
