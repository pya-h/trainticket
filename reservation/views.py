from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib import messages
from .models import Train, Person


def loginform(request):
    return render(request, 'auth/login.html')


def login(request):
    try:
        u = request.POST
        user = authenticate(request, username=u['name'], password=u['password'])
        if user is not None:
            auth_login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Error User is not registered/invalid")
    except Exception as ex:
        messages.error(request, ex.__str__())
    return render(request, 'auth/login.html')


def registerform(request):
    return render(request, 'auth/register.html')


def register(request):
    try:
        user = request.POST
        u = User.objects.create_user(user['name'], user['email'], user['password'])
        u.save()
        messages.success(request, 'Registration was successful!')
    except Exception as ex:
        messages.error(request, ex.__str__())
    return render(request, 'auth/register.html')


def logout(request):
    auth_logout(request)
    return render(request, 'auth/login.html')


def get_train(request, train_id):
    context = {}
    try:
        if not request.user.is_authenticated:
            messages.warning(request, "You must login first to see this train info.")
            return redirect('loginform')
        train = Train.objects.get(pk=train_id)
        persons = train.person_set.all()
        context['train'] = train
        context['persons'] = persons
    except Train.DoesNotExist:
        messages.error(request, "No such train or ticket!")
    except Exception as ex:
        messages.error(request, ex.__str__())
    return render(request, 'ticket/train.html', context)

temp = {}


def book(request):
    global temp
    if request.user.is_authenticated:
        t = Train.objects.filter(
            source=request.POST['source'], destination=request.POST['destination'])
        if len(t):
            temp['name'] = request.POST['name']
            temp['age'] = request.POST['age']
            temp['gender'] = request.POST['gender']

            return render(request, './trainsavailable.html', {'trains': t})
        else:
            messages.error(request, "Not Found")
            return redirect('home')
    else:
        messages.error(request, "This is not a valid account! You must login first!")
        return redirect('loginform')


def booking(request, train_id):
    tt = Train.objects.get(pk=train_id)
    if tt.seats_available == 0:
        return render(request, './error.html', {'msg': "Seats full"})
    tt.seats_available -= 1

    p = Person(train=tt, name=temp['name'], email=request.user.email, age=temp['age'], gender=temp['gender'])
    p.save()
    tt.save()
    messages.success(request, "Booked Successfully...Price to be paid is " + str(tt.price))
    return redirect('home')


def bookform(request):
    t = Train.objects.all()
    sources = []
    destinations = []
    for i in t:
        sources.append(i.source)
        destinations.append(i.destination)
    sources = list(set(sources))
    destinations = list(set(destinations))

    if request.user.is_authenticated:
        return render(request, './booking.html', {'sources': sources, 'destinations': destinations})
    else:
        messages.error(request, "You must login first!")
        return redirect('loginform')


def mybooking(request):
    if request.user.is_authenticated:
        p = Person.objects.filter(email=request.user.email)
        return render(request, './mybooking.html', {'persons': p})
    else:
        messages.error(request, "You must login first!")
        return redirect('loginform')
