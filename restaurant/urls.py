from django.urls import path
from restaurant.api_veiw import MenuView
from . import views
from .api_veiw import MenuView

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('menu/', views.menu_view, name='menu'),
    path('booking/', views.Booking, name='booking'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('api/menu/', views.menu_view, name='menu-list'),
    path('api_veiw/', MenuView.as_view()),
]