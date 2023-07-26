from django.shortcuts import render,redirect,get_object_or_404
from .models import Zapatilla,Ropa,Mochila,Producto, Abarrote,Servicio,Herramienta,Outdoor
from .forms import ContactoForm,ZapatillaForm,MochilaForm,RopaForm,ProductoForm,CustomUserCreationForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import Http404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, permission_required
# Create your views here.


def home(request):
    return render(request,'app/home.html')

def sobreNosotros(request):
    return render(request,'app/sobreNosotros.html')
@login_required
def contacto(request):
    data={
        'form':ContactoForm()
    }

    if request.method=='POST':
        formulario=ContactoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request,"Contacto enviado")
            return redirect(to="home")
        else:
            data["form"] = formulario
    return render(request,'app/contacto.html',data)

def producto(request):
    producto = Producto.objects.all()
    data={
        'producto':producto
    }
    return render(request,'app/producto.html',data)

def zapatillas(request):
    zapatillas = Zapatilla.objects.all()
    data={
        'zapatillas':zapatillas
    }
    return render(request,'app/zapatillas.html',data)

def about(request):
    return render(request,'app/about.html')

def abarrotes(request):
    abarrotes = Abarrote.objects.all()
    data={
        'abarrotes':abarrotes
    }
    return render(request,'app/abarrotes.html',data)

def servicios(request):
    servicios = Servicio.objects.all()
    data={
        'servicios':servicios
    }
    return render(request,'app/servicios.html',data)

def herramientas(request):
    herramientas = Herramienta.objects.all()
    data={
        'herramientas':herramientas
    }
    return render(request,'app/herramientas.html',data)

def outdoors(request):
    outdoors = Outdoor.objects.all()
    data={
        'outdoors':outdoors
    }
    return render(request,'app/outdoors.html',data)

def mochilas(request):
    mochilas=Mochila.objects.all()
    data={
        'mochilas':mochilas
    }
    return render(request,'app/mochilas.html',data)

def ropas(request):
    ropas=Ropa.objects.all()
    data={
        'ropas':ropas
    }
    return render(request,'app/ropas.html',data)

def catalogo(request):
    return render(request,'app/catalogo.html')

@login_required
def agregar_producto(request):
    data ={
        'form':ProductoForm()
    }

    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST,files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request,"Producto publicado")
            return redirect(to="home")
        else:
            data["form"]=formulario
    return render(request,'app/producto/agregar.html',data)


@login_required
def listar_producto(request):
    productos = Producto.objects.all()
    page = request.GET.get('page',1)

    try:
        paginator = Paginator(productos,5)
        productos = paginator.page(page)
    except:
        raise Http404
    data = {
        'productos':productos,
        'paginator':paginator
    }
    return render(request,'app/producto/listar.html',data)


@permission_required('app.change_producto')
def modificar_producto(request,id):
    producto=get_object_or_404(Producto,id=id)
    
    data= {
        'form':ProductoForm(instance=producto)
    }

    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST,instance=producto,files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "modificado correctamente")
            return redirect(to="listar_producto")
        data["form"]=formulario
    return render(request,'app/producto/modificar.html',data)

@permission_required('app.delete_producto')
def eliminar_producto(request,id):
    producto = get_object_or_404(Producto,id=id)
    producto.delete()
    messages.success(request,"eliminado correctamente")
    return redirect(to="listar_producto")


def registro(request):
    data = {
        'form':CustomUserCreationForm()
    }
    if request.method =='POST':
        formulario= CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"],password=formulario.cleaned_data["password1"])
            login(request,user)
            messages.success(request,"te has registrado correctamente")
            return redirect(to='home')
        data["form"]=formulario
    return render(request, 'registration/registro.html',data)