from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import ContactsView, ProductListView, ProductDetailView, CategoryListView, ProductUpdateView, \
    ProductCreateView, CategoryCreateView, ProductDeleteView, PublishProductView

app_name = CatalogConfig.name

urlpatterns = [
    path("", CategoryListView.as_view(), name="category_list"),
    path("category_create/", CategoryCreateView.as_view(), name="category_form"),
    path("contacts/", ContactsView.as_view(), name="contacts"),
    path("products/<int:pk>/", ProductListView.as_view(), name="products"),
    path("product_info/<int:pk>/", ProductDetailView.as_view(), name="product_info"),
    path("product_create/", ProductCreateView.as_view(), name="product_form"),
    path("product_update/<int:pk>/update", ProductUpdateView.as_view(), name="product_update"),
    path("product_delete/<int:pk>/delete", ProductDeleteView.as_view(), name="product_delete"),
    path("publish_product/<int:pk>/", PublishProductView.as_view(), name="publish_product"),
]
