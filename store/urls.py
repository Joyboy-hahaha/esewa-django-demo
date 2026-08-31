from django.urls import path
from . import views


urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('checkout/<int:product_id>/', views.checkout, name='checkout'),
    path('esewa/success/', views.esewa_success, name='esewa_success'),
    path('esewa/failure/', views.esewa_failure, name='esewa_failure'),
]