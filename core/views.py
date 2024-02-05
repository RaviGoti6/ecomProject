from django.shortcuts import render,HttpResponse
from core.models import Product, Category, Vendor, CartOrder, CartOrderItems, ProductImages, ProductReview, whishlist, Address


def index(request):
    # products = Product.objects.all().order_by("-id")

    products = Product.objects.filter(product_status="published", featured=True)

    context = {
        "products":products
    }
    return render(request, 'core/index.html', context)

def product_list_view(request):
    products = Product.objects.filter(product_status="published")

    context = {
        "products":products
    }
    return render(request, 'core/product-list.html', context)