from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, "home.html")


def contacts(request):
    if request.method == "POST":
        name = request.POST.get("name")
        return HttpResponse(f"Здравствуйте, {name}! Ваше сообщение принято!")
    return render(request, "contacts.html")
