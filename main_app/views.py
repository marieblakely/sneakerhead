from django.shortcuts import render
from django.http import HttpResponse


class Sneaker:  
  def __init__(self, style, number, description):
    self.name = style
    self.breed = number
    self.description = description
  

sneakers = [
  Sneaker('Bred', '11', 'Brand new with original packaging.'),
  Sneaker('Concord', '11', 'Brand new with original packaging.'),
  Sneaker('Red Cement', '4', 'Like new. Barely worn with original packaging.'),
  Sneaker('Chicago', '1', 'Worn. Does not have original packaging.')
]

# Create your views here.
def home(request):
  return HttpResponse('<h1>Hello Sneakerhead👟</h1>')

def about(request):
  return render(request, 'about.html')