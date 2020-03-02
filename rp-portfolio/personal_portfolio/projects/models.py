from django.db import models
from django.core.files.storage import FileSystemStorage

fs = FileSystemStorage(location='/home/nunoferreira/Desktop/django_practice/rp-portfolio/personal_portfolio/projects/static')    

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=20)
    photo = models.ImageField(storage=fs)

