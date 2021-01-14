from django.contrib import admin

from mensagem.models import (
    Conversa,
    Mensagem,
)
# Register your models here.

admin.site.register(Conversa)
admin.site.register(Mensagem)