from django.shortcuts import render



class Sneaker:  
  def __init__(self, style, number, description):
    self.style = style
    self.number = number
    self.description = description
  

sneakers = [
  Sneaker('Bred', '11', 'Brand new with original packaging.'),
  Sneaker('Concord', '11', 'Brand new with original packaging.'),
  Sneaker('Red Cement', '4', 'Like new. Barely worn with original packaging.'),
  Sneaker('Chicago', '1', 'Worn. Does not have original packaging.')
]

# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def sneaker_index(request):
  return render(request, 'sneakers/index.html', { 'sneakers': sneakers })