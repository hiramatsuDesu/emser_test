from django.urls import path
from persona.views import *

app_name = 'persona'

urlpatterns = [
    path('', index_persona, name='home'),
    path('crear', crearUsuario, name='crear'),
    path('borrar/<int:pk>', borrarUsuario, name='borrar'),
    path('lista', ver_lista_usuarios, name='ver_lista'),
    path('ver/<int:pk>', ver_detalle_usuario, name='ver_usuario'),
    path('modificar', editar_usuario, name='editar'),
    path('edita/<int:pk>', actualizar_usuario, name='actualizar')
    #path('lista', lista_usuarios)
]