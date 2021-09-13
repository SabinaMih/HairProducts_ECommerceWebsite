from django.urls import path
from . import views


app_name='shop'

urlpatterns = [
    path('', views.allProductCategories, name='allProductCategories'),
    path('<uuid:category_id>/', views.allProductCategories, name='products_by_category'),
    path('<uuid:category_id>/<uuid:product_id>/', views.product_details, name='product_details'),
    #path('<slug:slug>/', views.product_details, name='product_details'),
    path('apply/', views.voucher_apply, name='apply'),
    path('<uuid:pk>/review/', views.add_review_to_product, name='add_review_to_product'),
]