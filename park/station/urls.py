from django.urls import path
from . import views

urlpatterns = [
    path('station/', views.members, name='members'),
    path('inscription/', views.inscription, name='inscription'),
   # path('connecter/', views.connecter, name='connecter'),
]