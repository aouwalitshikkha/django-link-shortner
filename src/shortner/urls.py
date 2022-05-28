from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name ="home"),
    path('<code>/', views.link_redirect, name='link_redirect')

]