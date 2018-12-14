from . import views
from django.conf.urls import include, url
# Create your views here.

app_name='app'

urlpatterns = [
    url(r'^lista_clientes$', views.lista_clientes, name = "lista_clientes"),
    url(r'^$', views.menu_principal, name = "menu"),
    url(r'^registrar_tecnico',include('accounts.urls')),
    url(r'^registrar_cliente',views.registrar_cliente, name="registrar_cliente"),
    url(r'^asignar_tecnico',views.asignar_tecnico, name="asignar_tecnico"),
    url(r'^(?P<id_cliente>[\w]+)/$', views.ordenes_cliente, name="datos_cliente"),
    url(r'^(?P<id_cliente>[\w]+)/(?P<folio>[\w]+)$', views.detalle_orden, name="detalle_orden"),
    url(r'^(?P<id_cliente>[\w]+)/(?P<folio>[\w]+)$', views.detalle_orden, name="detalle_orden"),
    url(r'^registrar_orden', views.registrar_orden, name="registrar_orden")
]