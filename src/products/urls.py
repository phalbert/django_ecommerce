from django.urls import path

from . import views

app_name = 'products'
urlpatterns = [
    path('products/', views.ProductListView.as_view(), name='product-list'),
    path('products/featured', views.ProductFeaturedListView.as_view(), name='featured-list'),
    # path('products/<slug:pk>/', views.ProductDetailView.as_view(), name='product-detail'),
    path('products/<slug:slug>/', views.ProductDetailView.as_view(), name='product-slug')
]
