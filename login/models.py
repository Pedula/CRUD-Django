from django.db import models
from contato.models import Contato

# Create your models here.
class Login(models.Model):
	usuario = models.CharField(max_length =50)
	senha = models.CharField(max_length =50)
	status = models.BooleanField(default=True)
	fk = models.ForeignKey(Contato)

	def __unicode__(self):
		return self.usuario