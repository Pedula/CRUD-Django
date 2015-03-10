from django.conf.urls import patterns, include, url
from django.contrib import admin
from contato.models import Contato
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'first_django_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),


	url(r'^admin/', include(admin.site.urls)),
	url(r'^',include('contato.urls')),

	
)