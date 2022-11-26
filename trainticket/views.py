from django.shortcuts import render, redirect
from django.contrib import  messages
from reservation.models import Train


def home(request):
    trains = []
    try:
        if not request.user.is_authenticated:
            messages.warning(request, "First you need to login to your account. Then you can see trains list.")
            return redirect('loginform')
        trains = Train.objects.all()
    except Train.DoesNotExist:
        trains = []
    return render(request, 'home.html', {"trains": trains})


def about_us(request):
    return render(request, 'us/about.html')


def contact_us(request):
    return render(request, 'us/contact.html')
