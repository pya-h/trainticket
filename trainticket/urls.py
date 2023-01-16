
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('about/', views.about_us, name='about-us'),
    path('contact/', views.contact_us, name='contact-us'),
    path('search_form/', views.search_form, name='search-form'),

    path('search/', views.search, name='search'),
    path('reservation/', include('reservation.urls'))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
