from django.shortcuts import render,HttpResponse,redirect

#from . import forms.RegisterForm
from .forms import RegisterForm,LoginForm

from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate
from django.contrib import messages

# Create your views here.
def register(request):
  form = RegisterForm(request.POST or None)

  if form.is_valid():
    username = form.cleaned_data.get('username')
    password = form.cleaned_data.get('password')
    newUser = User(username = username)
    newUser.set_password(password)
    newUser.save()
    login(request, newUser) #login methodu automatic login yapacak register den sonra
    messages.success(request, 'Basariyla kayit oldunuz')
    return redirect('index')

  context = {
    'form': form
  }
  return render(request, 'register.html', context)

# def register(request):
#   if request.method == 'POST':
#     form = RegisterForm(request.POST)
#     if form.is_valid():
#       username = form.cleaned_data.get('username')
#       password = form.cleaned_data.get('password')
#       newUser = User(username = username)
#       newUser.set_password(password)
#       newUser.save()
#       login(request, newUser) #login methodu automatic login yapacak register den sonra
#       return redirect('index')

#     context = {
#       'form': form
#     }
#     return render(request, 'register.html', context)

#   else:
#     form = RegisterForm()

#     context = {
#       'form': form
#     }
#     return render(request, 'register.html', context)
def loginUser(request):
  form = LoginForm(request.POST or None)
  context = {
    'form': form
  }
  if form.is_valid():
    username = form.cleaned_data.get('username')
    password = form.cleaned_data.get('password')
  
    user = authenticate(username=username, password=password)
    if user is None:
      messages.info(request, 'Kullanici adi veya parola hatali')
      return render(request, 'login.html', context)
    messages.success(request, 'Basarili bir sekilde giris yapildi')
    login(request, user)
    return redirect('index')
  return render(request, 'login.html', context)

def logoutUser(request):
  pass