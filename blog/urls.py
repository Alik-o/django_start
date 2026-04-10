from django.urls import path

from catalog.apps import CatalogConfig
from blog.views import BlogListView, BlogDetailView, BlogCreateView, BlogUpdateView, BlogDeleteView

app_name = CatalogConfig.name

urlpatterns = [
    path("blog/", BlogListView.as_view(), name="blog_list"),
    path("blog/<int:pk>/", BlogDetailView.as_view(), name="blog_detail"),
    path("blog/blog_create/", BlogCreateView.as_view(), name="blog_form"),
    path("blog/<int:pk>/update/", BlogUpdateView.as_view(), name="blog_update"),
    path("blog/<int:pk>/delete/", BlogDeleteView.as_view(), name="blog_delete"),
]
