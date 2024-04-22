from django.test import TestCase

# Create your tests here.
    # FraseInline can handle a null FraseDb instance
    def test_handling_null_instance(self):
        import os
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "your_project.settings")
        import django
        django.setup()
    
        from django.contrib import admin
        from .models import FraseDb

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

        class FraseInline(admin.TabularInline):
            model=FraseDb
            extra = 1

        frase_inline = FraseInline()
        assert frase_inline.model == FraseDb
        assert frase_inline.extra == 1
