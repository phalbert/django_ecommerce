from django.urls import path

from . import views

app_name = 'products'
urlpatterns = [
    path('products/', views.ProductListView.as_view(), name='list'),
    path('products/featured', views.ProductFeaturedListView.as_view(), name='featured'),
    # path('products/<slug:pk>/', views.ProductDetailView.as_view(), name='product-detail'),
    path('products/<slug:slug>/', views.ProductDetailView.as_view(), name='detail'),
    path('products/search', views.ProductSearchListView.as_view(), name='search')
]
