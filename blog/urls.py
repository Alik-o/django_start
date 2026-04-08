from django.urls import path

from catalog.apps import CatalogConfig
from blog.views import blog

app_name = CatalogConfig.name

urlpatterns = [
    path("blog/", blog, name="blog"),
]
