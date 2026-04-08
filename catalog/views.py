from django.http import HttpResponse

from django.views.generic import ListView, DetailView, TemplateView

from catalog.models import Product, Category


class CategoryListView(ListView):
    model = Category
    template_name = 'category_list.html'


class ProductListView(ListView):
    model = Product
    template_name = 'products.html'

    def get_queryset(self):
        return Product.objects.filter(category_id=self.kwargs['pk'])


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_info.html'


class ContactsView(TemplateView):
    template_name = 'contacts.html'

    def post(self, request):
        name = request.POST.get("name")
        return HttpResponse(f"Здравствуйте, {name}! Ваше сообщение принято!")
