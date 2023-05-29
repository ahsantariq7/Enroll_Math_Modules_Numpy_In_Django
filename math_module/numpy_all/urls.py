
from django.urls import path
from numpy_all import views

urlpatterns = [
    path('',views.home, name='home'),

]