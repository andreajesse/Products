from django.shortcuts import redirect, render
from django.db.models import Q
from django.core.paginator import Paginator
from django.http import JsonResponse
import json
import datetime

from .models import * #insProduct, otcProduct, ProductType, Category, C 
from .forms import otcProductForm, insProductForm #, StatusForm

# Create your views here.

def home(request):
    return render(request, 'base/home.html')

# OTC PRODUCTS ------------------------------------------------------
def shop(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    products = otcProduct.active_objects.filter(
        Q(ProdType_Name__ProdType_Name__icontains=q) |
        Q(Cat_Name__Cat_Name__icontains=q) |
        Q(Prod_Name__icontains=q) 
    ).order_by('-date_created')

    #CATEGORIES
    prod_type = ProductType.objects.all()
    categories = Category.objects.all()

    #PAGE NAVIGATION
    paginator = Paginator(products, 9)
    page_number = request.GET.get('page')
    page_prod = paginator.get_page(page_number)

    context= {'prod_type': prod_type, 'categories': categories, 'products': products, 'page_prod': page_prod}
    return render(request, 'base/otc-products/shop.html', context)

	# for cart number (navbar)
    # '''data = cartData(request)

	# cartItems = data['cartItems']
	# order = data['order']
	# items = data['items']'''
	
	# if request.user.is_authenticated:
	# 	customer = request.user.customer
	# 	order, created = Order.objects.get_or_create(customer=customer, complete=False)
	# 	items = order.orderitem_set.all()
            # for cart number (navbar) -remove this line-
	# 	cartItems = order.get_cart_items
	# else:
	# 	items=[]
	# 	order =  {'get_cart_total':0, 'get_cart_items':0, 'pickup': False}
            # for cart number (navbar) -remove this line-
	# 	cartItems = order['get_cart_items']
		
	# products = Product.objects.all()
	# context = {'products':products, 'cartItems':cartItems}
	# return render(request, 'otc-products/store.html', context)

def shopIndivProduct(request, pk):
    product = otcProduct.active_objects.get(id=pk)

    #BROWSE OTHER PRODUCTS
    browse = otcProduct.active_objects.filter(
        Q(Cat_Name=product.Cat_Name) |
        Q(ProdType_Name=product.ProdType_Name)
    ).order_by('?').exclude(id=pk)

    context = {'product': product, 'browse': browse}
    return render(request, 'base/otc-products/shop_indiv_product.html', context)

def otcProducts(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    products = otcProduct.objects.all()
    
    search = otcProduct.objects.filter(
        Q(id__icontains=q) |
        Q(Prod_Name__icontains=q) |
        Q(ProdType_Name__ProdType_Name__icontains=q) |
        Q(Cat_Name__Cat_Name__icontains=q) 
    ).order_by('-date_created')
    
    #form = StatusForm()
    #if request.method == 'POST':
    #    form = StatusForm(request.POST)
    #    if form.is_valid():
    #        form.save()

    #PAGE NAVIGATION
    paginator = Paginator(search, 10)
    page_number = request.GET.get('page')
    page_prod = paginator.get_page(page_number)

    context = {'products': products, 'search': search, 'page_prod': page_prod}
    return render(request, 'base/otc-products/products.html', context)

def otc_indivProduct(request, pk):
    product = otcProduct.objects.get(id=pk)

    context = {'product': product}
    return render(request, 'base/otc-products/indiv_product.html', context)

def otc_createProduct(request):
    form = otcProductForm()
    if request.method == 'POST':
        form = otcProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('otc-products')

    context = {'form': form}
    return render(request, 'base/otc-products/product_form.html', context)

def otc_updateProduct(request, pk):
    product = otcProduct.objects.get(id=pk)
    form = otcProductForm(instance=product)

    if request.method == 'POST':
        form = otcProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('otc-products')

    context = {'form': form}
    return render(request, 'base/otc-products/product_form.html', context)

#def deleteProduct(request, pk):
#    product = otcProduct.objects.get(id=pk)
#    if request.method == 'POST':
#        product.delete()
#        return redirect('products')

#    return render(request, 'base/delete_product.html', {'obj': product})


# INSALON PRODUCTS ------------------------------------------------------
def insProducts(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    products = insProduct.objects.all()
    
    search = insProduct.objects.filter(
        Q(id__icontains=q) |
        Q(Prod_Name__icontains=q) |
        Q(ProdType_Name__ProdType_Name__icontains=q) |
        Q(Cat_Name__Cat_Name__icontains=q) 
    ).order_by('-date_created')
    
    #PAGE NAVIGATION
    paginator = Paginator(search, 10)
    page_number = request.GET.get('page')
    page_prod = paginator.get_page(page_number)

    context = {'products': products, 'search': search, 'page_prod': page_prod}
    return render(request, 'base/ins-products/products.html', context)

def ins_indivProduct(request, pk):
    product = insProduct.objects.get(id=pk)

    context = {'product': product}
    return render(request, 'base/ins-products/indiv_product.html', context)

def ins_createProduct(request):
    form = insProductForm()
    if request.method == 'POST':
        form = insProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ins-products')

    context = {'form': form}
    return render(request, 'base/ins-products/product_form.html', context)

def ins_updateProduct(request, pk):
    product = insProduct.objects.get(id=pk)
    form = insProductForm(instance=product)

    if request.method == 'POST':
        form = insProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('ins-products')

    context = {'form': form}
    return render(request, 'base/ins-products/product_form.html', context)

#  ------------------------------------------------------

#CART RENDER VIEW
def cart(request):
	'''data = cartData(request)

	cartItems = data['cartItems']
	order = data['order']
	items = data['items']'''
	#context = {'items':items, 'order':order, 'cartItems':cartItems}

	if request.user.is_authenticated:
		customer = request.user.customer
		order, created = Order.objects.get_or_create(customer=customer, complete=False)
		items = order.orderitem_set.all()
		cartItems = order.get_cart_items
	else:
		items=[]
		order =  {'get_cart_total':0, 'get_cart_items':0, 'pickup': False}
		cartItems = order['get_cart_items']
		
	context = {'items':items, 'order':order, 'cartItems':cartItems}
	return render(request, 'base/otc-products/cart.html', context)

#CHECKOUT RENDER VIEW
def checkout(request):
	if request.user.is_authenticated:
		customer = request.user.customer
		order, created = Order.objects.get_or_create(customer=customer, complete=False)
		items = order.orderitem_set.all()
		cartItems = order.get_cart_items
	else:
		items=[]
		order =  {'get_cart_total':0, 'get_cart_items':0, 'pickup': False}
		cartItems = order['get_cart_items']
		
	context = {'items':items, 'order':order, 'cartItems':cartItems}
	return render(request, 'base/otc-products/checkout.html', context)

#PURCHASES RENDER VIEW
def mypurchases(request):
	if request.user.is_authenticated:
		customer = request.user.customer
		order, created = Order.objects.get_or_create(customer=customer, complete=False)
		items = order.orderitem_set.all()
		cartItems = order.get_cart_items
	else:
		items=[]
		order =  {'get_cart_total':0, 'get_cart_items':0, 'pickup': False}
		cartItems = order['get_cart_items']
		
	context = {'items':items, 'order':order, 'cartItems':cartItems}
	return render(request, 'base/otc-products/mypurchases.html', context)


#SALES INVOICE RENDER VIEW
def salesinvoice(request):
	context = {}
	return render(request, 'otc-products/salesinvoice.html', context)

#UPDATE ITEM RENDER VIEW
def updateItem(request):
    ## parse since it is a string value
	data = json.loads(request.body)
    ## get the product id and action
	productId = data['productId']
	action = data['action']

	print('Action:', action)
	print('Product ID:', productId)

    ## query customer
	customer = request.user.customer
    ## get the product we are passing in
	product = otcProduct.objects.get(id=productId)
    ## create or add to order
	order, created = Order.objects.get_or_create(customer=customer, complete=False)

	orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    ## quantity
	if action == 'add':
		orderItem.quantity = (orderItem.quantity + 1)
	elif action == 'remove':
		orderItem.quantity = (orderItem.quantity - 1)

	orderItem.save()

	if orderItem.quantity <= 0:
		orderItem.delete()

	return JsonResponse('Item was added', safe=False)

def processOrder(request):
	transaction_id = datetime.datetime.now().timestamp()
	data = json.loads(request.body)

	if request.user.is_authenticated:
		customer = request.user.customer
		order, created = Order.objects.get_or_create(customer=customer, complete=False)
	else:
		customer, order = guestOrder(request, data)

	total = float(data['form']['total'])
	order.transaction_id = transaction_id

	if total == order.get_cart_total:
		order.complete = True
	order.save()

	if order.pickup == True:
		PickUp.objects.create(
		customer=customer,
		order=order,
		pickup=data['pickup']['pickupdate'],
		)

	return JsonResponse('Order Complete!', safe=False)

def orders(request):
    orders = Order.objects.all()
    orderitems = OrderItem.objects.all()

    context = {'orders': orders, 'orderitems': orderitems}
    return render(request, 'base/otc-products/orders.html', context)
