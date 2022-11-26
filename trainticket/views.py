from django.shortcuts import render, redirect
from django.contrib import  messages


def home(request):
    if not request.user.is_authenticated:
        messages.warning(request, "First you need to login to your account. Then you can see trains list.")
        return redirect('loginform')
    return render(request, 'home.html')


def about_us(request):
    return render(request, 'us/about.html')


def contact_us(request):
    return render(request, 'us/contact.html')
