from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import Template, Context
from django.contrib.auth.forms import UserCreationForm
from .models import *
from django.contrib import messages


# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            messages.success(request, f'Usuario {username} creado')
            return redirect('feed')
    else:
        form = UserCreationForm()

    context = {'form': form}
    return render(request, "templates/register.html", context)

"""""
def login(request):
    return render(request, 'user/login.html')


def home(request):
    return render(request, 'user/home.html')


def grupos(request):
    return render(request, 'user/grupos.html')


def convocatorias(request):
    return HttpResponse("Convocatorias")


def resultados(request):
    return render(request, "user/resultados.html")

"""