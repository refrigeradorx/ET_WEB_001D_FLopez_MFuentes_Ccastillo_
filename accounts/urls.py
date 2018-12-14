
from . import views
from django.conf.urls import url
# Create your views here.

app_name='accounts'

urlpatterns = [
    url(r'^registrar_tecnico$', views.registrar_tecnico, name="registrar_tecnico"),
    url(r'^$', views.loginView, name="login"),
    url(r'^logout$', views.logoutView, name="logout"),

]