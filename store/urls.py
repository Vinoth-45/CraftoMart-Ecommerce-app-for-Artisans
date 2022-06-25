from django.urls import path
from ArtisanDashboard import views as artisan_module_views
from . import views


urlpatterns = [
	#Leave as empty string for base url
	path('', views.index, name="home_index"),
	path('store/', views.store, name="store"),
	path('cart/', views.cart, name="cart"),
	path('login/', views.customer_login, name="customer_login"),
	path('register/', views.register, name="customer_register"),
	path('checkout/', views.checkout, name="checkout"),
	path('update_item/', views.updateItem, name="update_item"),
	path('process_order/', views.processOrder, name="process_order"),

	#Fro artisan module...
	path('artisan_signup/', artisan_module_views.register, name="artisan_register"),
	path('artisan_signin/', artisan_module_views.login, name="artisan_login"),

]