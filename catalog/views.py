from django.http import HttpResponse
from django.shortcuts import render

from catalog.models import Product


def home(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, "home.html", context)


def contacts(request):
    if request.method == "POST":
        name = request.POST.get("name")
        return HttpResponse(f"Здравствуйте, {name}! Ваше сообщение принято!")
    return render(request, "contacts.html")


def products(request, pk):
    products = Product.objects.filter(category_id=pk)
    context = {'products': products}
    return render(request, "products.html", context)


def product_info(request, pk):
    product = Product.objects.get(pk=pk)
    context = {'product': product}
    return render(request, "product_info.html", context)
