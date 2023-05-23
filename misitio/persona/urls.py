from django.urls import path
from persona.views import *

app_name = 'persona'

urlpatterns = [
    path('', index_persona, name='home'),
    path('crear', crearUsuario, name='crear'),
    path('borrar/<int:pk>', borrarUsuario, name='borrar'),
    path('lista', ver_lista_usuarios, name='ver_lista'),
    path('ver/<int:pk>', ver_detalle_usuario, name='ver_usuario'),
    path('listaedicion', vista_editar, name='actualizar'),
    path('editar/<int:pk>', fun_editar, name='editaru'),
    path('editarus/<int:pk>', editarUsuario, name='editarus'),
]