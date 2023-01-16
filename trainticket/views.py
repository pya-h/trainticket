from django.shortcuts import render, redirect
from django.contrib import  messages
from datetime import datetime
from reservation.models import Train
from django.http import HttpResponse, JsonResponse
import pytz

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


def search(request):
    if not request.user.is_authenticated:
        messages.warning(request, "First you need to login to your account. Then you can see trains list.")
        return redirect('loginform')
    queryset = Train.objects.all()
    if request.POST:
        source = request.POST.get('source')
        destination = request.POST.get('destination')
        sd = request.POST.get('start_date')
        st = request.POST.get('start_time')
        ed = request.POST.get('end_date')
        et = request.POST.get('end_time')
        start_date = None
        end_date = None
        if sd:
            if not st:
                st = "00:00"
            year, month, day = [int(x) for x in sd.split('-')]
            hour, minutes = [int(x) for x in st.split(':')]
            start_date = datetime(year, month, day, hour, minutes, tzinfo=pytz.UTC)
        if ed and et:
            if not st:
                et = "00:00"
            year, month, day = [int(x) for x in ed.split('-')]
            hour, minutes = [int(x) for x in et.split(':')]
            end_date = datetime(year, month, day, hour, minutes, tzinfo=pytz.UTC)
        if source:
            queryset = queryset.filter(source=source)
        if destination :
            queryset = queryset.filter(destination=destination)
        if start_date and end_date:
            queryset = queryset.filter(time__gte=start_date, time__lte=end_date).values()
        elif start_date and not end_date:
            queryset = queryset.filter(time__gte=start_date).values()
        elif not start_date and end_date:
            queryset = queryset.filter(time__lte=end_date).values()
            
    return render(request, "search/search_result.html", {"trains": queryset})
    # return render(queryset, 'ticket/search.html')

def search_form(request):
    if not request.user.is_authenticated:
        messages.warning(request, "First you need to login to your account. Then you can see trains list.")
        return redirect('loginform')
    return render(request, "search/search.html")
