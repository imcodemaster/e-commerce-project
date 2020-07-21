from django.shortcuts import render
from django.http import JsonResponse
import json
from .models import * 
from .models import Product
from django.views.generic import ListView, DetailView, View

def home(request):
	if request.user.is_authenticated:
		customer = request.user.customer
		order , created = Order.objects.get_or_create(customer = customer , complete = False)
		items = order.orderitem_set.all()
		cartItems = order.get_cart_items
	else : 
		order = {'get_cart_total':0, 'get_cart_items': 0, 'shipping':False}
		items = []
		cartItems = order['get_cart_items']

	products = Product.objects.all()
	context = {'products':products, 'cartItems': cartItems}
	return render(request, 'store/home.html', context)

def about(request):
	if request.user.is_authenticated:
		customer = request.user.customer
		order , created = Order.objects.get_or_create(customer = customer , complete = False)
		items = order.orderitem_set.all()
		cartItems = order.get_cart_items
	else : 
		order = {'get_cart_total':0, 'get_cart_items': 0, 'shipping':False}
		items = []
		cartItems = order['get_cart_items']

	context = {'cartItems': cartItems}

	return render(request, 'store/about.html', context)

def details(request):
	if request.user.is_authenticated:
		customer = request.user.customer
		order , created = Order.objects.get_or_create(customer = customer , complete = False)
		items = order.orderitem_set.all()
		cartItems = order.get_cart_items
	else : 
		order = {'get_cart_total':0, 'get_cart_items': 0, 'shipping':False}
		items = []
		cartItems = order['get_cart_items']

	context = {'cartItems': cartItems}
	return render(request, 'store/details.html', context)

def store(request):
		if request.user.is_authenticated:
			customer = request.user.customer
			order , created = Order.objects.get_or_create(customer = customer , complete = False)
			items = order.orderitem_set.all()
			cartItems = order.get_cart_items
		else : 
			items = []
			order = {'get_cart_total':0, 'get_cart_items': 0, 'shipping':False}
			cartItems = order['get_cart_items']
			
		products = Product.objects.all()
		context = {'products':products, 'cartItems':cartItems}
		return render(request, 'store/store.html', context)

def cart(request):
	if request.user.is_authenticated:
		customer = request.user.customer
		order , created = Order.objects.get_or_create(customer = customer , complete = False)
		items = order.orderitem_set.all()
		cartItems = order.get_cart_items
	else : 
		order = {'get_cart_total':0, 'get_cart_items': 0, 'shipping':False}
		items = []
		cartItems = order['get_cart_items']

	context = {'items' : items, 'order' : order, 'cartItems':cartItems}
	return render(request, 'store/cart.html', context)

def checkout(request):
	if request.user.is_authenticated:
		customer = request.user.customer
		order , created = Order.objects.get_or_create(customer = customer , complete = False)
		items = order.orderitem_set.all()
		cartItems = order.get_cart_items
	else : 
		order = {'get_cart_total':0, 'get_cart_items': 0, 'shipping':False}
		items = []
		cartItems = order['get_cart_items']

	context = {'items' : items, 'order' : order , 'cartItems':cartItems}
	return render(request, 'store/checkout.html', context)

def updateItem(request):
	data = json.loads(request.body)
	productId = data['productId']
	action = data['action']
	print('Action:', action)
	print('Product:', productId)

	customer = request.user.customer
	product = Product.objects.get(id=productId)
	order, created = Order.objects.get_or_create(customer=customer, complete=False)

	orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

	if action == 'add':
		orderItem.quantity = (orderItem.quantity + 1)
	elif action == 'remove':
		orderItem.quantity = (orderItem.quantity - 1)

	orderItem.save()

	if orderItem.quantity <= 0:
		orderItem.delete()

	return JsonResponse('Item was added', safe=False)


def search(request):

	try:
		qur = request.GET.get('q')
	except:
		qur = None

	if qur :
		qur = request.GET.get('q').lower()
		template = 'store/results.html'
		result = [item for item in Product.objects.all() if qur in item.name.lower()]
		


	else:
		template = 'store/home.html'
		result = {}
	
	return render(request, template, {"result": result })


class ProductDetailView(DetailView):
    model = Product
    template_name = "product_detail.html"
