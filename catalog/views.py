from itertools import product

from django.http import HttpResponse
from django.urls import reverse_lazy

from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView

from catalog.forms import ProductForm, CategoryForm
from catalog.models import Product, Category


class CategoryListView(ListView):
    model = Category
    template_name = 'category_list.html'


class CategoryCreateView(CreateView):
    model = Category
    template_name = 'category_form.html'
    form_class = CategoryForm
    context_object_name = 'category'
    success_url = '/'


class ProductListView(ListView):
    model = Product
    template_name = 'products.html'

    def get_queryset(self):
        return Product.objects.filter(category_id=self.kwargs['pk'])


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_info.html'


class ProductCreateView(CreateView):
    model = Product
    template_name = 'product_form.html'
    form_class = ProductForm
    context_object_name = 'product'
    success_url = reverse_lazy('catalog:category_list')


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'product_form.html'
    context_object_name = 'product'
    success_url = reverse_lazy('catalog:category_list')


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'product_confirm_delete.html'
    success_url = reverse_lazy('catalog:category_list')


class ContactsView(TemplateView):
    template_name = 'contacts.html'

    def post(self, request):
        name = request.POST.get("name")
        return HttpResponse(f"Здравствуйте, {name}! Ваше сообщение принято!")
