from django import forms
from django.forms import ModelForm

from mensagem.models import (
    Mensagem,
    Conversa,
)


class MensagemForm(ModelForm):

    class Meta:
        model = Mensagem
        fields = ['texto', 'imagem']


        widgets = {
            'texto' : forms.TextInput(attrs={
                'id' : 'texto_field',
                'placeholder' :'mensagem',
            }),
        }
    def __init__(self, *args, **kwargs):
        super(MensagemForm, self).__init__(*args, **kwargs)
        # self.fields['texto'].widget = forms.TextInput(attrs={
        #     'id' : 'texto_field',
        #     'placeholder' :'mensagem',
        # })
    
        