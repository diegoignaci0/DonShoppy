from django.contrib import admin
from .models import Marca,Zapatilla,Ropa,Mochila,Contacto,Producto,Servicio,Abarrote,Herramienta
# Register your models here.

class ProductoAdmin(admin.ModelAdmin):
    list_display=["nombre","precio","marca"]
    list_editable=["precio"]
    search_fields=["nombre"]


admin.site.register(Marca)
admin.site.register(Zapatilla,ProductoAdmin)
admin.site.register(Ropa,ProductoAdmin)
admin.site.register(Mochila,ProductoAdmin)
admin.site.register(Contacto)
admin.site.register(Producto,ProductoAdmin)
admin.site.register(Servicio,ProductoAdmin)
admin.site.register(Abarrote,ProductoAdmin)
admin.site.register(Herramienta,ProductoAdmin)
