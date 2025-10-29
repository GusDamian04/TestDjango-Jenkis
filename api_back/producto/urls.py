from django.urls import path
from .views import ProductListCreateView

urlpatterns = [
    path('productos/', ProductListCreateView.as_view(), name='product-list-create'),
]