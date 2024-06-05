from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Sneaker
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm





# Create your views here.
def about(request):
  return render(request, 'about.html')

def sneaker_index(request):
  sneakers = Sneaker.objects.all()
  return render(request, 'sneakers/index.html', { 'sneakers': sneakers })

def sneaker_detail(request, sneaker_id):
  sneaker = Sneaker.objects.get(id=sneaker_id)
  return render(request, 'sneakers/detail.html', { 'sneaker': sneaker })

class Home(LoginView):
  template_name = 'home.html'

class SneakerCreate(CreateView):
  model = Sneaker
  fields = '__all__'
  success_url = '/sneakers/'

  def form_valid(self, form):
    form.instance.user = self.request.user  
    return super().form_valid(form)

class SneakerUpdate(UpdateView):
  model = Sneaker
  fields = ['style', 'number', 'description']

class SneakerDelete(DeleteView):
  model = Sneaker
  success_url = '/sneakers/'  

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('sneaker-index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'signup.html', context)  