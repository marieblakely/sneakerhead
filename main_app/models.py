from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Sneaker(models.Model):
  style = models.CharField(max_length=100)
  number = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  user = models.ForeignKey(User, on_delete=models.CASCADE)


  def __str__(self):
    return self.style
  
  def get_absolute_url(self):
    return reverse('sneaker-detail', kwargs={'sneaker_id': self.id})