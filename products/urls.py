from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('create', views.create, name='create'),
    path('<int:product_id>/upvote', views.upvote, name='upvote'),
    path('<slug:slug>', views.product_detail, name='product-detail'),
    path('category/<slug:slug>', views.category_detail, name='category-detail'),
    path('all/categories', views.categories, name='categories'),
    path('add/comment', views.add_comment, name='add-comment'),
]
