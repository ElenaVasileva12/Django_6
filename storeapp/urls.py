from django.contrib import admin
from django.urls import path,include
from .views import index,view_client,post_product,view_client_day

urlpatterns = [
    path('',index,name='index'),     #http://127.0.0.1:8088/store/
    path('client/',view_client,name='client'),
    path('client2/<int:day_>',view_client_day,name='client2'),
    path('product/',post_product,name='product'),

]
