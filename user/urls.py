from django.urls import path
from . import views

urlpatterns = [
    path('', views.profiles, name = 'profiles'),
    path('profile/<str:pk>/', views.userProfile, name = 'user-profile'),
    
    path('login', views.loginPage, name = 'login'),
    path('logout', views.logoutPage, name = 'logout'),
    path('user-registration', views.user_registration, name = 'user-registration'),
    path('admin-registration', views.admin_registration, name = 'admin-registration'),
    path('edit-user-profile/<str:pk>/', views.edit_user_profile, name = 'edit-user-profile'),
    path('add-rank/', views.create_rank, name = 'add-rank'),
    path('delete-rank/<str:pk>/', views.delete_rank, name = 'delete-rank')
]