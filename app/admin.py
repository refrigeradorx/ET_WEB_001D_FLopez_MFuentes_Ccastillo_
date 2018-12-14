from django.contrib import admin
from .models import Cliente, OrdenTrabajo, Ascensor, Detalle_Orden

admin.site.register(Cliente)
admin.site.register(OrdenTrabajo)
admin.site.register(Ascensor)
admin.site.register(Detalle_Orden)


# Register your models here.
