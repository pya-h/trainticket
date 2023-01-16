from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib import messages
from .models import Train


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
        context['train'] = train
    except Train.DoesNotExist:
        messages.error(request, "No such train or ticket!")
    except Exception as ex:
        messages.error(request, ex.__str__())
    return render(request, 'ticket/train.html', context)

temp = {}

def book(request):
    global temp
    if request.user.is_authenticated:
        if request.POST:
            train_id = request.POST.get("train_id")
            print(train_id)
            train = None
            try:
                train = Train.objects.get(pk=train_id)
            except Exception as ex:
                train = None
                messages.error(request, ex.__str__())
            if train.seats_available <= 0:
                messages.error("There is no empty seats for you in this train!")
                return redirect(train.url())

            if train:
                for booker in train.bookers.all():
                    if booker.id == request.user.id:
                        messages.error(request, "You have reserved this train before!")
                        break
                else:
                    train.bookers.add(request.user)
                    train.seats_available -= 1
                    train.save()
                    messages.success(request, "This train has been reserved successfully!")
                return redirect(train.url())
            else:
                messages.error(request, "There is no such train!")
                return redirect('home')
    else:
        messages.error(request, "This is not a valid account! You must login first!")
        return redirect('loginform')

    return redirect(train.url())
