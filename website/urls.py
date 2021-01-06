from django.urls import path
from . import views

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
    path('order/', views.order_now, name="order"),
    path('order/<slug>/', views.single_slug, name="slug"),
    path('order/<slug>/<int:id>/add', views.add_to_card, name="add"),

]
