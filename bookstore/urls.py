from django import views
from django.urls import path
from .import views
urlpatterns = [
    path('dashboard', views.dashboard),
    path('books', views.books),
    path('customers/<str:pk>', views.customer),

]
