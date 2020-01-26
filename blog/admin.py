from django.contrib import admin
from .models import Artikel

class ArtikelforAdmin(admin.ModelAdmin):
	readonly_fields = ['slug','updated','published']

# Register your models here.
admin.site.register(Artikel,ArtikelforAdmin)