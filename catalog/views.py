from itertools import product

from django.http import HttpResponse
from django.urls import reverse_lazy

from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView

from catalog.forms import ProductForm, CategoryForm
from catalog.models import Product, Category


class CategoryListView(ListView):
    model = Category


class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    context_object_name = 'category'
    success_url = '/'


class ProductListView(ListView):
    model = Product
    template_name = 'catalog/products.html'

    def get_queryset(self):
        return Product.objects.filter(category_id=self.kwargs['pk'])


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_info.html'


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    context_object_name = 'product'
    success_url = reverse_lazy('catalog:category_list')


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    context_object_name = 'product'
    success_url = reverse_lazy('catalog:category_list')


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:category_list')


class ContactsView(TemplateView):
    template_name = 'catalog/contacts.html'

    def post(self, request):
        name = request.POST.get("name")
        return HttpResponse(f"Здравствуйте, {name}! Ваше сообщение принято!")
