from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Contato(models.Model):
	nome = models.CharField(max_length =50)
	fixo = models.CharField(max_length = 50)
	cel = models.CharField(max_length = 20)
	email = models.EmailField()
	endereco = models.CharField(max_length = 100)	

	def __unicode__(self):
		return self.nome