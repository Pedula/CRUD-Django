from django.shortcuts import render_to_response, get_object_or_404 as g404
from login.models import Login
from django.http import HttpResponse
from forms import LoginForm, PerfilForm
from django.template import RequestContext
from django.http import HttpResponseRedirect as red
from django.contrib.auth import authenticate, login, logout


def login(request):
	form = PerfilForm()
	next = request.REQUEST.get('next', '/')
	e = ""
	if request.POST:
			form = PerfilForm(request.POST)
			if form.is_valid():
					e = form.cleaned_data['usuario']
					p = form.cleaned_data['senha']
					ah = authenticate(usuario=e, senha=p)
					if ah is not None:
							if ah.is_active:
									login(request, ah)
									return red(next)
	context = RequestContext(request,{'form': form, 'next': next})
	return render_to_response('entrar.html',context)



def sair(request):
	logout(request)
	return red('/entrar/')