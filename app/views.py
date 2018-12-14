from django.shortcuts import render,redirect
from . import views
from .models import Cliente, OrdenTrabajo
from .forms import registrarCliente , asignarTecnico, ordenForm, detalleForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from accounts.models import User

# Create your views here.

@login_required
def registrar_cliente (request):
    if request.method =='POST':
        form = registrarCliente(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Se ha agregado un cliente exitosamente')
            return redirect('app:registrar_cliente')
    else:
        form = registrarCliente()
    return render(request,'registrar_cliente.html',{'form':form})

@login_required
def asignar_tecnico (request):
    if request.method =='POST':
        form = asignarTecnico(request.POST)
        if form.is_valid():
            cli = form.cliente._get_choices()
            usr = form.users._choices
            for var in usr:
                cli.var
                #form.save(commit=False)
                messages.success(request,'Se ha asignado un tecnico exitosamente')
                return redirect('app:asignar_tecnico')
    else:
        #clientes = Cliente.objects.all()
      #  Users = User.objects.all()
        form = asignarTecnico()
    return render(request,'asignar_tecnico.html',{'form':form})#{'clientes':clientes, 'Users':Users, 'form':form})


@login_required
def menu_principal (request):
    return render (request,'menu.html')


@login_required
def lista_clientes (request):
    usr = request.user
    clientes = Cliente.objects.filter(tecnico__pk=usr.id)
    #filtrar lista de clientes segun tecnico id
    return render (request,'lista_clientes.html', {'clientes':clientes})



@login_required
def ordenes_cliente (request,id_cliente):
    usr = request.user
    cli = Cliente.objects.get(id=id_cliente)
    ordenes = OrdenTrabajo.objects.filter(cliente__pk=cli.id)
    #ordenes = Ordenes.objects.get(cliente_id=id_cliente)
    #filtrar ordenes segun id_cliente
    #filtrar lista de clientes segun tecnico
    return render (request,'ordenes_cliente.html', {'Ordenes':ordenes})    


@login_required
def detalle_orden (request,id_cliente,folio):
    usr = request.user
    cli = Cliente.objects.get(id=id_cliente)
    ordenes = OrdenTrabajo.objects.filter(tecnico__pk=usr.id)
    #ordenes = Ordenes.objects.get(cliente_id=id_cliente)
    #filtrar ordenes segun id_cliente
    #filtrar lista de clientes segun tecnico
    return render (request,'detalle_orden.html', {'Ordenes':ordenes}) 


@login_required
def registrar_orden (request):
    if request.method == 'POST':
        form = ordenForm(request.POST)
        detalle = detalleForm(request.POST)
        if form.is_valid() and detalle.is_valid():
            form.save()
            detalle.save()
            messages.success(request,'Se ha agregado una orden exitosamente')
            return redirect('app:registrar_orden')
    else:
        form = ordenForm()
        detalle = detalleForm()
    return render(request,'registrar_orden.html',{'form':form,'detalle':detalle})
    #usr = request.user
    #cli = Cliente.objects.get(id=id_cliente)
    #ordenes = OrdenTrabajo.objects.filter(tecnico__pk=usr.id)
    #ordenes = Ordenes.objects.get(cliente_id=id_cliente)
    #filtrar ordenes segun id_cliente
    #filtrar lista de clientes segun tecnico
    #return render (request,'registrar_orden.html') 