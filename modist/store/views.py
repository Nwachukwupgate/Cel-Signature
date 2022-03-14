from django.shortcuts import render, get_object_or_404
from .models import *
from django.http import Http404, HttpResponse, JsonResponse
from django.core.paginator import Paginator
import json
# Create your views here.

def index(request):
    trendp = TrendingProduct.objects.all()
    prod = Product.objects.all()
    testa = Testimony.objects.all()
    return render(request, 'index.html',{'tp':trendp, 'pr':prod,'ta':testa})

def shop(request):

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order={'get_cart_items':0, 'get_cart_total':0, 'shipping':False}
        cartItems = order['get_cart_items']

    ite = Shop.objects.all()

    paginator = Paginator(ite, 12)
    page = request.GET.get('page')
    items = paginator.get_page(page)
    return render(request, 'shop.html',{'item':items, 'cartItems':cartItems})

def details(request, link_id):
    det = get_object_or_404(ShopDetails, shop__pk=link_id)
    return render(request, 'product-single.html', {'detail':det})


def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order={'get_cart_items':0, 'get_cart_total':0, 'shipping':False}
        cartItems = order['get_cart_items']
    return render(request, 'cart.html',{'items':items, 'order':order, 'cartItems':cartItems})

def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order={'get_cart_items':0, 'get_cart_total':0, 'shipping':False}
        cartItems = order['get_cart_items']

    return render(request, 'checkout.html',{'items':items, 'order':order, 'cartItems':cartItems})

def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    print('Action:', action)
    print('Product:', productId)

    customer= request.user.customer
    product = Shop.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)

    orderItem, created = OrderItem.objects.get_or_create(order=order, shop=product)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('Item was added', safe=False)