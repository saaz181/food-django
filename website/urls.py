from django.urls import path, include
from django.views.generic import TemplateView
from . import views

app_name = 'website'

urlpatterns = [
    path('', views.home, name="home"),
    path('contact.html/', views.contact, name="contact"),
    path('about.html/', views.about, name="about"),
    path('blog.html/', views.blog, name="blog"),
    path('recipe.html/', views.recipe, name="recipe"),
    path('book.html/', views.book, name="book"),
    path('register/', views.register, name="register"),
    path('login/', views.login_request, name="login"),
    path('logout/', views.logout_request, name="logout"),

]
