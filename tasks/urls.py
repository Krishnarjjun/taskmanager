from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('create/', views.task_create, name='task_create'),
    path('login/', views.login, name='login'),
    path('home/', views.home, name='home'),
    # path for products for ecommerce app
    path('products/', views.products, name='products'),
    path('update/<int:task_id>/', views.task_update, name='task_update'),
    path('delete/<int:task_id>/', views.task_delete, name='task_delete'),
]
