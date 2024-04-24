from django.contrib import admin
from .models import AutorDb,FraseDb

# Register your models here.
admin.site.site_header = "Administrador sefogi"
admin.site.index_title = "sefogiadmin"
admin.site.site_title = "administrador"
class FraseInline(admin.TabularInline):
     model=FraseDb
     extra = 1


class AutorAdmin(admin.ModelAdmin):
    
   fields =["Nombre","Fecha_nacimiento","Fecha_fallecimiento","Profesion","Nacionalidad"]

   list_display = ["Nombre", "Fecha_nacimiento"]

   inlines=[FraseInline]
   
   #crear acciones
   
   def actualizar_o(self,request,queryset):
       for obj in queryset:
           if "O" in obj.Nombre:
               Nombre1 = obj.Nombre
               obj.Nombre = Nombre1.replace("O", "o")
               obj.save()  
               
               
       self.message_user(request,"Exitosamente")
       
        
   actualizar_o.short_description="Actualizar letras O"
    
   actions=["actualizar_o"]
        
    
   

admin.site.register(AutorDb, AutorAdmin)

@admin.register(FraseDb)
class FraseAdmin(admin.ModelAdmin):
    fields=["Cita", "Autor_fk"]
    list_display=["Cita"]
