from django.urls import path, include
from . import views
from django.contrib import admin 
from .views import *

urlpatterns = [
    path('', views.home, name='home'),
    path('viewWindow', views.getproduct, name='getproduct'),
    path('adminpage', views.login, name='login'),
    path('signUp',views.upload,name='upload'),
    path('Contact',views.Contact,name='Contact'),
    path('userMessage',views.userMessage,name='userMessage'),
    path('logout',views.logout,name='logout'),
    path('Search',views.search,name='search'),
    path('updatestatus',views.updatestatus,name='updatestatus'),
    path('orderitem', views.vieworderdetails, name='vieworderdetails'),
    path('homesearch', views.honmesearch, name='homesearch'),
    path('Review', views.reviewupload, name='reviewupload'),
    path('gallery', views.gallery, name='gallery'),
    path('placeorder', views.gallery, name='placeOrder'),
    path('checkoutOrder', views.checkout, name='checkout'),
    path('return', views.notify_url_process, name='returnfun'),
    path('orderDetails', views.orderDetails, name='orderDetails'),
    
]


