from django.db import models
from django.utils import timezone
import datetime

# Create your models here.

class News(models.Model):
    text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    photo = models.ImageField(upload_to='news')

    def __str__(self):
        return self.text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Pilot(models.Model):
    pilot_name = models.CharField(max_length=200)

    def __str__(self):
        return self.pilot_name

class Car(models.Model):
    pilot_id = models.ForeignKey(Pilot, on_delete=models.CASCADE)
    car_model = models.CharField(max_length=200)

    def __str__(self):
        return self.car_model


