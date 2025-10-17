from django.urls import path
from .views import RegisterView, profile_view, login_view

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', login_view, name='login'),  # new login endpoint
    path('profile/', profile_view, name='user-profile'),
]
