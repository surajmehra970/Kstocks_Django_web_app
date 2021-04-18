from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home,name='stockinfo-home'),
    path('profile/',views.profi,name='profile')

]