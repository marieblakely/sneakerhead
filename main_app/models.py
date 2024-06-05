from django.db import models

# Create your models here.
class Sneaker(models.Model):
  style = models.CharField(max_length=100)
  number = models.CharField(max_length=100)
  description = models.TextField(max_length=250)


  def __str__(self):
    return self.style