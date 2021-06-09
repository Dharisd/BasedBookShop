from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Product
from django.views.generic import ListView,DetailView

def index(request):
    template = loader.get_template('shop/index.html')
    products = Product.objects.filter(featured=True)
    context = {
        "products":products
    }

    return HttpResponse(template.render(context,request))

class ProductListView(ListView):
    template_name = "shop/list.html"
    context_object_name = "products"
    paginate_by = 10
    model = Product


class ProductDetailView(DetailView):
    template_name = "shop/details.html"
    context_object_name = "product"
    model = Product



class ProductSearchView(ListView):
    template_name = "shop/search.html"
    context_object_name = "products"
    paginate_by = 10
    model = Product

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        
        #Add search query to context
        search_query = self.request.GET.get('query', None)
        if search_query is not None:
            context['query'] = search_query

        
        return context

    def get_queryset(self):
        if self.request.method == 'GET':
            queryset = Product.objects.all()
            search_query = self.request.GET.get('query', None)
            #append search logic here
            if search_query is not None:
                queryset = queryset.filter(name__icontains=search_query)

            return queryset