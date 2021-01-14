from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm


class user_login_form(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']

        widgets = {
            'password' : forms.PasswordInput()
        }


class user_register_form(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']

        widgets = {
            'password' : forms.PasswordInput()
        }
    def save(self, commit=True):
        user = super(user_register_form, self).save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user