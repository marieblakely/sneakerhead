from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('sneakers/', views.sneaker_index, name='sneaker-index'),
  path('sneakers/<int:sneaker_id>/', views.sneaker_detail, name='sneaker-detail'),
]