from django.urls import path
from . import views
from store import views as storeViews
urlpatterns = [
	#Leave as empty string for base url
	path('dashboard/', views.dashboard, name="artisan_dashboard"),
	path('artisan_signup/', views.register, name="artisan_register"),
	path('artisan_signin/', views.login, name="artisan_login"),
	path('', storeViews.index, name="home_index"),
	path('addProduct/',views.addproduct, name="add_product"),
]