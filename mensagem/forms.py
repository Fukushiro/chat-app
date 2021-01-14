from django import forms
from django.forms import ModelForm

from mensagem.models import (
    Mensagem,
    Conversa,
)


class MensagemForm(ModelForm):

    class Meta:
        model = Mensagem
        fields = ['texto']