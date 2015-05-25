from django.shortcuts import render_to_response, get_object_or_404 as g404
from contato.models import Contato
from django.http import HttpResponse
from forms import ClienteForm
from django.template import RequestContext
from django.http import HttpResponseRedirect
# from django.contrib.auth.decorators import login_required, permission_required
# Create your views here.


# @login_required
def listar_contatos(request):
	contatos = Contato.objects.all().order_by("nome")
	return render_to_response('list.html',{'contatos':contatos})


# @login_required
def criar_contatos(request):
	form = ClienteForm(request.POST or None)
	
	if request.method == 'POST' and form.is_valid():
		form.save()
		return HttpResponseRedirect('/contatos/')

	context = RequestContext(request, {'form': form})
	return render_to_response('criar.html', context)



# @login_required
def editar_contato(request, id):
	contato = Contato.objects.get(id__exact = id)
	form = ClienteForm(request.GET,instance=contato)

	if form.is_valid():
		form.save()
		return HttpResponseRedirect('/contatos/')
	
	else:
		form = ClienteForm(instance=contato)

	context = RequestContext(request, {'form': form})
	return render_to_response('editar.html', context)


# @login_required
def excluir_contato(request, id):
	contato = Contato.objects.get(id__exact = id)
	
	if request.method == "POST":
		contato.delete()
		return HttpResponseRedirect('/contatos/')

	context = RequestContext(request, {'contato': contato})
	return render_to_response('excluir.html', context)


# @login_required
def index(request):

	return HttpResponseRedirect('/contatos/')