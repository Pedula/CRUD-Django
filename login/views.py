from django.shortcuts import render_to_response, get_object_or_404 as g404
from login.models import Login
from django.http import HttpResponse
from forms import LoginForm, PerfilForm
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login as authlogin


def login(Request):
	form = LoginForm()
	return render_to_response('entrar.html', {'form': form})
