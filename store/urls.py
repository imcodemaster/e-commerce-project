from django.urls import path
from . import views
from .views import ProductDetailView
from . import models
from .models import *

urlpatterns = [
        #Leave as empty string for base url
	path('', views.home, name="home"),
	path('about/', views.about, name="about"),
	path('details/', views.details , name = 'details' ),
	path('cart/', views.cart, name="cart"),
	path('store/', views.store, name="store"),
	path('checkout/', views.checkout, name="checkout"),
	path('update_item/', views.updateItem, name="update_item"),
	path('s/', views.search, name="search"),
	path('product_detail/<int:pk>/', ProductDetailView.as_view(), name='product'),


]