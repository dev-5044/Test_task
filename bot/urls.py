from django.urls import path
from .views import AssetLIstView, AssetUpdateView, AssetCreateView

urlpatterns = [
    path('home/', AssetLIstView.as_view()),
    path('update/<int:pk>/', AssetUpdateView.as_view(), name='update'),
    path('create/', AssetCreateView.as_view(), name='create')
]