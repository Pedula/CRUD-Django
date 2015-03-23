from django.conf.urls import patterns, include, url


urlpatterns = patterns('login.views',
    

   	url(r'^entrar/','login'),
	url(r'^sair/','sair'),
	
)