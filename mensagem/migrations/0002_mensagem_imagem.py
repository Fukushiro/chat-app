# Generated by Django 3.1.5 on 2021-01-16 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mensagem', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mensagem',
            name='imagem',
            field=models.ImageField(blank=True, null=True, upload_to='mensagem/imagens'),
        ),
    ]
