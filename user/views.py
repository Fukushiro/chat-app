from django.shortcuts import render, redirect
from django.contrib.auth import (
    authenticate,
    login,
    logout,
)

from user.forms import (
    user_login_form,
    user_register_form,
)


from mensagem.views import (
    home,
)
# Create your views here.

def user_login(request):

    if request.method == 'POST':
        u = authenticate(username=request.POST['username'], password=request.POST['password'])
        if u is not None:
            login(request, u)
            return redirect(home)

    form = user_login_form()
    c = {
        'form' : form,
    }
    return render(request, 'user/login/login.html', c)

def user_register(request):

    if request.method == 'POST':
        form = user_register_form(request.POST or None)
        if form.is_valid():
            form.save()


    form = user_register_form()

    c = {
        'form' : form,
    }
    return render(request, 'user/register/register.html', c)