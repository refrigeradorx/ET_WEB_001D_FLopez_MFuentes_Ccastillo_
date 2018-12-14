from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegistrarTecnico, LoginForm
from django.contrib.auth import login, logout, decorators
from django.contrib.auth.decorators import login_required
from django.contrib import messages
#from ..app.forms import registrar_tecnico

@login_required
def registrar_tecnico (request):
    if request.method =='POST':
        form = RegistrarTecnico(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Se ha registrado un tecnico exitosamente')
            return redirect('accounts:registrar_tecnico')
    else:
        form = RegistrarTecnico()
    return render(request, 'registrar_tecnico.html',{'form':form})


def loginView (request):
    if request.method == 'POST':
        form = LoginForm(data = request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            return redirect('app:menu')
    else:
        form = LoginForm ()
    return render(request, 'index.html',{'form':form})    


def logoutView (request):
    if request.method == 'POST':
        logout(request)
        return redirect('/') 
