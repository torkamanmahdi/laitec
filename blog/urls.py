from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('create/', views.create_post, name='create_post'), # for create dummy posts
    # path('category/<int:pk>/', views.cat_view, name='cat_view'),
    path('slider/<int:pk>/', views.slider, name='slider'),
]