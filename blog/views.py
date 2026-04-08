from django.shortcuts import render

def blog(request):
    return render(request, "base_blog.html")
