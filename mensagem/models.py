from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Conversa(models.Model):
    usuario1 = models.ForeignKey(User ,  on_delete=models.CASCADE, related_name='usuario1')
    usuario2 = models.ForeignKey(User ,  on_delete=models.CASCADE, related_name='usuario2')

class Mensagem(models.Model):
    conversa = models.ForeignKey(Conversa ,  on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    data = models.DateTimeField(auto_now=False, auto_now_add=False)
    texto = models.CharField(max_length=250)