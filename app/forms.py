from .models import Cliente, OrdenTrabajo, Detalle_Orden
from django import forms
from accounts.models import User



class registrarCliente(forms.ModelForm):
    
    class Meta:
        model = Cliente
        fields = ('nombre', 'direccion', 'ciudad', 'comuna', 'telefono', 'correo', )


class asignarTecnico(forms.Form):
    users = forms.ModelMultipleChoiceField(queryset=User.objects.all())
    cliente = forms.ModelChoiceField(queryset = Cliente.objects.all())

class ordenForm (forms.ModelForm):
    fecha = forms.DateTimeField(widget=forms.SelectDateWidget(attrs={'class':'input-100'},))    

    
    hora_inicio=forms.DateField(widget=forms.DateTimeInput(attrs={'placeholder':'Hora inicio','class':'input-100'},),label="")
    hora_termino=forms.DateField(widget=forms.DateTimeInput(attrs={'placeholder':'Hora termino','class':'input-100'},),label="")
    nom_cliente=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Nombre cliente','class':'input-100'},),label="")

    class Meta:
        model = OrdenTrabajo
        fields = ('folio','cliente','tecnico','fecha','hora_inicio','hora_termino','nom_cliente')
    


    
class detalleForm (forms.ModelForm):
    #fecha = forms.DateTimeField(widget=forms.SelectDateWidget(attrs={'class':'input-100'},))    
    #email=forms.EmailField(widget=forms.EmailInput(attrs={'class':'input-100'},),label="")
    #username=forms.EmailField(widget=forms.EmailInput(attrs={'placeholder':'Correo electronico','class':'form-control'},),label="")
    
    class Meta:
        model = Detalle_Orden
        fields = ('folio','fallas_detectadas','reparaciones_efectuadas','piezas_cambiadas','ascensor')