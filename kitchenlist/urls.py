from django.urls import path
from .views import KitchenListView, KitchenListDetailView

urlpatterns = [
    path('', KitchenListView.as_view(), name='kitchenlist'),
    path('<int:pk>/', KitchenListDetailView.as_view(), name='kitchenlist-detail'),
]
