from django.urls import path

from . import views

app_name = 'products'
urlpatterns = [
    path('products/', views.ProductListView.as_view(), name='product-list'),
    path('products/<slug:pk>/', views.ProductDetailView.as_view(), name='product-detail')
]
