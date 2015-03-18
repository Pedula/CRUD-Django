from django.shortcuts import render,render_to_response, get_object_or_404 as g404
from login.models import Login
from django.http import HttpResponse
from forms import LoginForm, PerfilForm
from django.template import RequestContext
from django.http import HttpResponseRedirect as red
from django.contrib.auth import authenticate, login, logout


def login(request):
	form = LoginForm(data=request.POST) 
	return render(request, "entrar.html", {"form": LoginForm()})

def sair(request):
	logout(request)
	return red('/entrar/')
