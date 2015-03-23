from django.conf.urls import patterns, include, url


urlpatterns = patterns('contato.views',
    

   	url(r'^$','index'),
    url(r'^contatos/$','listar_contatos', name='listar_contatos'),
	url(r'^contato/criar/$','criar_contatos', name='criar_contatos'),
	url(r'^contato/editar/(?P<id>\d+)$','editar_contato', name= 'editar_contato'),
	url(r'^contato/excluir/(?P<id>\d+)$','excluir_contato', name='excluir_contato'),
	
)