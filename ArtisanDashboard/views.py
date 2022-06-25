from multiprocessing import context
from turtle import update
from django.shortcuts import redirect, render
from .models import *
from store.models import *

def register(request):
	if request.method == "POST":
		artisan_name = request.POST['art_name']
		email = request.POST['art_email']
		password = request.POST['password']
		confirmpassword = request.POST['confirmpassword']
		compy_name = request.POST['compy_name']
		phno = request.POST['art_phno']
		zip = request.POST['zip_code']
		address = request.POST['address']
		if confirmpassword == password:
			artisan = Artisans(artisan_name=artisan_name,artisan_email=email,password=password,artisan_phno = phno,company_name = compy_name,company_address = address,zip_code=zip)
			artisan.register()
			return redirect('artisan_login')
	return render(request, 'artisan_registration.html')	
def login(request):
	if request.method == "POST":
		art_name = request.POST['art_name']
		password = request.POST['password']

		artisan = Artisans.objects.filter(password = password)
		if artisan is not None:
			art = artisan[0].artisan_name
			if art_name == art:
				request.session['artisan_name'] = art
				return redirect (dashboard)
	return render(request, 'artisan_login.html')	

def dashboard(request):
	if request.session['customer_logged_in'] == True:
		art_name = request.session['artisan_name']
		products = Product.objects.filter(prd_addedBy = art_name)
		orders = OrderItem.objects.filter(ord_prd_addedBy = art_name)				
		context = {'products':products,
				'orders':orders,
				"art_name" : art_name}
		return render(request, 'dashboard.html', context)
def addproduct(request):
	art_name = request.session['artisan_name']
	if request.method == "POST":
		prd_name = request.POST['prd_name']
		prd_price = request.POST['pirce']
		prd_image = request.POST['prd_image']
		prd_art_name = request.POST['art_name']

		product = Product(name = prd_name,
							price = prd_price,
							image = prd_image,
							prd_addedBy = prd_art_name)
		product.save()
		return redirect(dashboard)
	return render(request, 'addProduct.html',context={'art_name':art_name})		