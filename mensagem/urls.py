from django.contrib import admin
from django.urls import path
from mensagem.views import (
    home,
    conversa,
    conversa_mensagem,
    conversa_mensagem_post,
)


urlpatterns = [
    path('', home, name='home'),
    path('conversa/<int:idConversa>', conversa, name='conversa'),

    path('conversa/adicionar/<int:conversa_id>',conversa_mensagem, name='conversa_mensagem'),

    path('conversa/adicionarpost/<int:conversa_id>',conversa_mensagem_post, name='conversa_mensagem_post'),
]
