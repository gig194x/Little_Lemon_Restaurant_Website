from urllib import request

from django.shortcuts import render
from restaurant.forms import BookingForm
from restaurant.models import MenuModel

# Create your views here.


def home(request):
    return render(request, "restaurant/home.html")

def about(request):
    return render(request, "restaurant/about.html")


def menu_view(request):
    items = MenuModel.objects.all()
    return render(request, 'restaurant/menu.html', {'menu': items})


####################################################################3333

from pyexpat.errors import messages
from django.shortcuts import redirect, render
from .forms import BookingForm
# Create your views here.
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import BookingForm  # Make sure your form is imported


def Booking(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Booking submitted successfully!")
            return redirect("Booking")  # your URL name
    else:
        form = BookingForm()

    return render(request, "restaurant/book.html", {"form": form})







# registration view
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

def register(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = User.objects.create_user(username=username, password=password)
        user.save()
        return redirect('login')

    return render(request, "restaurant/register.html")


# login view
from django.contrib.auth.decorators import login_required
@login_required
def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')

    return render(request, "restaurant/login.html")

# logout view
def logout_view(request):
    logout(request)
    return redirect('login')