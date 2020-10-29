from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    # Static Routes
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    # Cat Routes
    path('cats/index/', views.cats_index, name='cats_index'),
    path('cats/new/', views.add_cat, name='add_cat'),
    path('cats/<int:cat_id>/delete/', views.delete_cat, name='delete_cat'),
    path('cats/<int:cat_id>/', views.cats_detail, name='detail'),
    path('cats/<int:cat_id>/edit/', views.edit_cat, name='edit_cat'),
    # Cat Feeding
    path('cats/<int:cat_id>/add_feeding/', views.add_feeding, name='add_feeding'),
    # Cat Toys
    path('cats/<int:cat_id>/assoc_toy/<int:toy_id>/', views.assoc_toy, name="assoc_toy"),
    # Auth
    path('accounts/signup', views.signup, name='signup'),
]
