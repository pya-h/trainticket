from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Train(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    source = models.CharField(max_length=50)
    destination = models.CharField(max_length=50)
    time = models.DateTimeField()
    price = models.FloatField(default=120)
    seats_available = models.IntegerField()
    image = models.ImageField(upload_to='photos/tickets', null=True, blank=True)
    bookers = models.ManyToManyField(User)
    def url(self):
        return reverse('train_id', args=[self.id,])

    def book_url(self):
        return reverse('book', args=[self.id, ])
