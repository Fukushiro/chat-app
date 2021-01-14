from django.shortcuts import render, redirect, HttpResponse
from django.db.models import Q
from django.http import JsonResponse
from django.contrib.auth.models import User
import datetime


from mensagem.models import (
    Conversa,
    Mensagem,
)

from mensagem.forms import (
    MensagemForm,
)
# Create your views here.


def home(request):

    if request.method == 'POST':
        usuario = User.objects.get(username=request.POST['nome'])
        conversa = Conversa(usuario1 = request.user, usuario2 = usuario)
        conversa.save()
        return redirect('home')

    user = request.user
    conversas = Conversa.objects.filter(Q(usuario1=user) | Q(usuario2=user))
    
    

    c = {
        'conversas' : conversas,
        'user' : user,
    }
    return render(request, 'mensagem/home.html', c)

def conversa(request, idConversa):
    conversa = Conversa.objects.get(id=idConversa)

    
    if request.method == 'POST':
        mensagem = Mensagem(conversa=conversa, usuario=request.user, data = datetime.datetime.now(), texto=request.POST['texto'])
        mensagem.save()
        return redirect('conversa', idConversa)
    form = MensagemForm()
    mensagens = Mensagem.objects.filter(conversa=conversa)



    c = {
        'mensagens' : mensagens,
        'form' : form,
        'user' : request.user,
        'conversa' : conversa,
    }
    return render(request, 'mensagem/conversa/conversa.html', c)


def conversa_mensagem(request, conversa_id):
    conversa = Conversa.objects.get(id=conversa_id)
    if request.GET['inserir'] == 'true':
        print('foi')
        mensagem = Mensagem(conversa=conversa, usuario=request.user, data = datetime.datetime.now(), texto=request.GET['texto'])
        mensagem.save()

    mensagens = Mensagem.objects.filter(conversa=conversa)
    c = {
        'mensagens' : mensagens,
    }
    
    return render(request, 'mensagem/conversa/teste.html', c)