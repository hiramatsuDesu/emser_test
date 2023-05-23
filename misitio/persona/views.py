from django.shortcuts import render, redirect, redirect, get_object_or_404
from django.urls import reverse
from .models import Persona
from .forms import PersonaModelForm


# Create your views here.
def index_persona(request):
    return render(request, 'persona/home.html')

def crearUsuario(request):
    persona_lista = Persona.objects.all()

    form = PersonaModelForm()

    if(request.method == 'POST'):
        print("ha ingresado al metodo post ")

        form = PersonaModelForm(request.POST)
        if(form.is_valid()):
            form.save()
        else:
            print(form.errors)
    context = {
        'form': form,
        'persona_lista':persona_lista
    }
    return render(request, 'persona/crear.html', context)


def borrarUsuario(request, pk):
    Persona.objects.get(pk=pk).delete()

    persona_lista = Persona.objects.all()
    context = {
        'persona_lista':persona_lista
    }
    #return render(request, 'persona/crear.html')
    #return redirect(reverse('persona: borrar', kwargs = {'pk':pk}))
    #return index_persona(request)
    #return redirect(reverse('persona:crear', kwargs='pk':pk))
    return redirect('persona:crear')

    
def ver_lista_usuarios(request):
    persona_lista = Persona.objects.all()
    context = {
        'persona_lista':persona_lista
    }
    return render(request, 'persona/lista.html', context)


def ver_detalle_usuario(request, pk):
    persona = Persona.objects.get(pk=pk)

    context = {
        'persona':persona
    }
    return render(request, 'persona/detalle.html', context)



def vista_editar(request, pk=None):
    persona = Persona.objects.all()
    context = {
        'per_lista':persona
    }
    return render(request, 'persona/editar.html', context)


"""
def fun_editar(request, pk):
    persona = Persona.objects.get(pk = pk)

    form = PersonaModelForm(instance = persona)

    if(request.method == 'POST'):
        form = PersonaModelForm(request.POST, instance = persona)

        if(form.is_valid()):
            form.save()
        else:
            print(form.errors)
    context ={
        'form':form
    }
    return render(request, 'persona/modalmodificar.html', context)

"""

def fun_editar(request, pk=None):

    if(pk!=None):
        persona = Persona.objects.get(pk = pk)

        form = PersonaModelForm(instance = persona)

        if(request.method == 'POST'):
            form = PersonaModelForm(request.POST, instance = persona)

            if(form.is_valid()):
                form.save()
            else:
                print(form.errors)
            return render(request, 'persona/modal.html', {'form':form})
    context ={
        'form':form,
        'per':persona
    }
    return render(request, 'persona/modal.html', context)




def editarUsuario(request, pk):

    if(pk !=None):
        print(pk)

        persona = Persona.objects.get(pk = pk)

        print(pk)
        form = PersonaModelForm()

    if(request.method == 'POST'):
        print("ha ingresado al metodo post ")
        print(request)

        form = PersonaModelForm(request.POST, instance = persona)
        if(form.is_valid()):
            form.save()
        else:
            print(form.errors)

        persona_lista = Persona.objects.all()
    
    context = {
        'form': form,
        'persona_lista': persona_lista
    }
    
    return render(request, 'persona/lista.html', context)