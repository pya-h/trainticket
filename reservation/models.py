from django.db import models
from django.urls import reverse


# Create your models here.
class Train(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    source = models.CharField(max_length=50)
    destination = models.CharField(max_length=50)
    time = models.TimeField(auto_now=False, auto_now_add=False)
    price = models.FloatField(default=120)
    seats_available = models.IntegerField()
    image = models.ImageField(upload_to='photos/tickets', null=True, blank=True)

    def url(self):
        return reverse('train_id', args=[self.id,])


class Person(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=128)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    email = models.EmailField(max_length=384)
    booking_datetime = models.DateTimeField(auto_now_add=True)  # check this!
    train = models.ForeignKey(Train, on_delete=models.CASCADE)
