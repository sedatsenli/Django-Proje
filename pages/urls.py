from django.urls import path
from . import views

urlpatterns = [
    path('', views.indexx, name="indexx"),
    path('indexx', views.indexx, name="indexx"),
    path('menu', views.menu, name="menu"),
    path('contact', views.contact, name="contact"),
    path('today-special', views.today_special, name="today-special"),
   # path('/login', views.login, name="login"),
   # path('signup', views.signup, name="signup"),
 #   path('sepet', views.sepet, name="sepet"),
]