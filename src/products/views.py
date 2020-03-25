from django.shortcuts import render
from django.views import generic
from .models import Product
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

class ProductListView(generic.ListView):
    model = Product
    context_object_name = 'products'
    paginate_by = 10
    ordering = ['-id']
      
    def get_context_data(self, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)
        items = self.get_queryset()
        page = self.request.GET.get('page')
        paginator = Paginator(items, self.paginate_by)
        try:
            items = paginator.page(page)
        except PageNotAnInteger:
            items = paginator.page(1)
        except EmptyPage:
            items = paginator.page(paginator.num_pages)
        context['products'] = items
        return context

class ProductFeaturedListView(generic.ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'products/featured_list.html'
    paginate_by = 10
    ordering = ['-id']

    def get_queryset(self, *args, **kwargs):
        return Product.objects.featured()
      

class ProductDetailView(generic.DetailView):
    model = Product
    context_object_name = 'products'
    paginate_by = 10
    ordering = ['-id']

    def get_context_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        items = self.get_queryset()
        page = self.request.GET.get('page')
        paginator = Paginator(items, self.paginate_by)
        try:
            items = paginator.page(page)
        except PageNotAnInteger:
            items = paginator.page(1)
        except EmptyPage:
            items = paginator.page(paginator.num_pages)
        context['products'] = items
        return context

class ProductSearchListView(generic.ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'products/search_results.html'
    # paginate_by = 10
    # ordering = ['-id']

    def get_queryset(self, *args, **kwargs):
        query = self.request.GET.get('q', None)
        return Product.objects.search(query)