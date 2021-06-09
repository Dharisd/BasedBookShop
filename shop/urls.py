from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import index,ProductDetailView,ProductListView,ProductSearchView

app_name = "shop-urls"

urlpatterns = [
    path('', index, name='index'),
    #view Product details
    path("details/<int:pk>",ProductDetailView.as_view(),name="product-details"),
    path("products/",ProductListView.as_view(),name="product-list"),
    path("search/",ProductSearchView.as_view(),name="product-search")


]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)