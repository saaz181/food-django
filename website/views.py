from django.shortcuts import render, redirect
from django.core.mail import send_mail
from datetime import datetime
from .forms import SignUpForm
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .models import Food, FoodCategory


def add_to_card(request, id):
    pass



def single_slug(request, slug):
    categories = [c.category_slug for c in FoodCategory.objects.all()]
    if slug in categories:
        matching_foods = Food.objects.filter(food_category__category_slug=slug)
        foods_url = {}
        for food in matching_foods.all():
            foods_url[food] = food

        return render(request, template_name="website/order_food.html", context={"foods": foods_url})



def order_now(request):
    return render(request, template_name="website/order.html", context={"foods": FoodCategory.objects.all})


def home(request):
    return render(request, template_name="website/home.html", context={})


def contact(request):
    if request.method == "POST":
        Name = request.POST['Name']
        Email = request.POST['Email']
        Phone = request.POST['Phone']
        Message = request.POST['Message']

        # Send an email
        send_mail(
            "Message from: " + Name,  # subject,
            Message,  # message,
            Email,  # from email,
            ['saliaz.mg326@gmail.com']  #, "2ndemail@info.com"],  # To email
        )

        return render(request, template_name="website/contact.html", context={"name": Name})

    else:
        return render(request, template_name="website/contact.html", context={})


def about(request):
    return render(request, template_name="website/about.html", context={})


def blog(request):
    time = datetime.now().strftime('%d %b %Y')
    return render(request, template_name="website/blog.html", context={'time': time})


def recipe(request):
    return render(request, template_name="website/recipe.html", context={})


def book(request):
    if request.method == "POST":
        Name = request.POST['Name']
        Email = request.POST['Email']
        Phone = request.POST['Phone']
        address = request.POST['address']
        schedule = request.POST['schedule']
        date = request.POST['date']

        message_book = f"Name: {Name}" + "\n" + f"Phone: {Phone}" +\
                       "\n" + f"Address: {address}" + "\n" + f"Schedule: {schedule}" + "\n" +\
                       f"Date: {date}"
        # Send an email
        send_mail(
            "Booking Table Request",  # subject,
            message_book,  # message,
            Email,  # from email,
            ['saliaz.mg326@gmail.com']  #, "2ndemail@info.com"],  # To email
        )

        return render(request, template_name="website/book.html", context={"name": Name,
                                                                           "email": Email,
                                                                           "phone": Phone,
                                                                           "address": address,
                                                                           "schedule": schedule,
                                                                           "date": date,
                                                                           })
    else:
        return render(request, template_name="website/book.html", context={})


def register(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            # messages.success(request, f"New Account Created: {username}")
            login(request, user)
            # messages.info(request, f"You're logged in: {username}")
            return redirect("/")
        # else:
        #     for msg in form.error_messages:
        #         messages.error(request, f"{msg}: {form.error_messages[msg]}")

    form = SignUpForm
    return render(request, template_name="website/register.html", context={"form": form})


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are logged in: {username}")
                return redirect('/')
            else:
                messages.error(request, "Invalid password or username")
        else:
            messages.error(request, "Invalid password or username")

    form = AuthenticationForm()
    return render(request, template_name="website/login.html", context={"form": form})


def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("/")


