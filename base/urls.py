from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='landing'),
    path('dashboard/', views.dashboard, name = 'home'),
    path('room/<str:pk>/', views.room, name = 'room'),
    path('create-room', views.create_room, name = 'create-room'),
    path('update-room/<str:pk>/', views.update_room, name = 'update-room'),
    path('delete-room/<str:pk>/', views.delete_room, name = 'delete-room'),
    path('delete-message/<str:pk>/', views.delete_message, name = 'delete-message'),
    path('shop/', views.shop, name='shop'),
    path('post-item/', views.post_item, name = 'post-item'),
    path('buy-item/<str:pk>/', views.buy_item, name = 'buy'),

    path('visualize', views.visualize, name = 'visualize'),
]