from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import ContactsView, ProductListView, ProductDetailView, CategoryListView

app_name = CatalogConfig.name

urlpatterns = [
    path("", CategoryListView.as_view(), name="category_list"),
    path("contacts/", ContactsView.as_view(), name="contacts"),
    path("products/<int:pk>/", ProductListView.as_view(), name="products"),
    path("product_info/<int:pk>/", ProductDetailView.as_view(), name="product_info"),
]
