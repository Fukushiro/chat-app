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
        if User.objects.filter(username=request.POST['nome']).count() > 0:
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
        print(request.FILES)
        
        mensagem_form = MensagemForm(request.POST or None, request.FILES or None)

        if mensagem_form.is_valid():
            m = mensagem_form.save(commit=False)
            m.conversa = conversa
            m.usuario = request.user
            m.data = datetime.datetime.now()


            m.save()
        #mensagem = Mensagem(conversa=conversa, usuario=request.user, data = datetime.datetime.now(), texto=request.POST['texto'], request.FILES or None)
        #mensagem.save()
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


def conversa_mensagem(request, conversa_id):#refresh
    conversa = Conversa.objects.get(id=conversa_id)
    
    # if request.GET['inserir'] == 'true':
    #     print(request.GET)
    #     mensagem_form = MensagemForm(request.GET or None, request.FILES or None)

    #     if mensagem_form.is_valid():
    #         m = mensagem_form.save(commit=False)
    #         m.conversa = conversa
    #         m.usuario = request.user
    #         m.data = datetime.datetime.now()


    #         m.save()
        #mensagem = Mensagem(conversa=conversa, usuario=request.user, data = datetime.datetime.now(), texto=request.GET['texto'])
        #mensagem.save()

    mensagens = Mensagem.objects.filter(conversa=conversa)
    c = {
        'mensagens' : mensagens,
    }
    
    return render(request, 'mensagem/conversa/teste.html', c)

def conversa_mensagem_post(request, conversa_id):#enviar msg
    conversa = Conversa.objects.get(id=conversa_id)
    
    
    mensagem_form = MensagemForm(request.POST or None, request.FILES or None)

    if mensagem_form.is_valid():
        m = mensagem_form.save(commit=False)
        m.conversa = conversa
        m.usuario = request.user
        m.data = datetime.datetime.now()


        m.save()
        #mensagem = Mensagem(conversa=conversa, usuario=request.user, data = datetime.datetime.now(), texto=request.GET['texto'])
        #mensagem.save()

    mensagens = Mensagem.objects.filter(conversa=conversa)
    c = {
        'mensagens' : mensagens,
    }
    
    return render(request, 'mensagem/conversa/teste.html', c)