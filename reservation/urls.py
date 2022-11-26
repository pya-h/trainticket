from django.urls import path, include
from . import views

urlpatterns = [
    path('loginform/', views.loginform, name="loginform"),
    path('login/', views.login, name="login"),
    path('registerform/', views.registerform, name="registerform"),
    path('register/', views.register, name="register"),
    path('logout/', views.logout, name="logout"),
    path('<train_id>', views.get_train, name="train_id"),
    path('book/', views.book, name="book"),
    path('bookform/', views.bookform, name="bookform"),
    path('mybooking/', views.mybooking, name="mybooking"),
    path('booking/<train_id>', views.booking, name="booking")

]
