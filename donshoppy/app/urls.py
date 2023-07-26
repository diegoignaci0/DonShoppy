from django.urls import path
from .views import home,sobreNosotros,contacto,producto,zapatillas,catalogo,ropas,mochilas,agregar_producto,listar_producto,modificar_producto,eliminar_producto,registro,abarrotes,servicios,herramientas,outdoors,about

urlpatterns = [
    path('', home,name="home"),
    path('sobreNosotros/',sobreNosotros,name="sobreNosotros"),
    path('contacto/',contacto,name="contacto"),
    path('producto/',producto,name="producto"),
    path('zapatillas/',zapatillas,name="zapatillas"),
    path('mochilas/',mochilas,name="mochilas"),
    path('abarrotes/',abarrotes,name="abarrotes"),
    path('servicios/',servicios,name="servicios"),
    path('ropas/',ropas,name="ropas"),
    path('herramientas/',herramientas,name="herramientas"),
    path('outdoors/',outdoors,name="outdoors"),
    path('catalogo/',catalogo,name="catalogo"),
    path('agregar_producto/',agregar_producto,name="agregar_producto"),
    path('listar_producto/',listar_producto,name="listar_producto"),
    path('modificar_producto/<id>/',modificar_producto,name="modificar_producto"),
    path('eliminar_producto/<id>/',eliminar_producto,name="eliminar_producto"),
    path('registro/',registro,name="registro"),
    path('about/',about,name="about"),
]
