# Generated by Django 3.1.5 on 2021-01-13 19:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Conversa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='usuario1', to=settings.AUTH_USER_MODEL)),
                ('usuario2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='usuario2', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Mensagem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateTimeField()),
                ('texto', models.CharField(max_length=250)),
                ('conversa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mensagem.conversa')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
