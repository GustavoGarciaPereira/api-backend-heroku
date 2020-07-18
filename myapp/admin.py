from django.contrib import admin

# Register your models here.

from .models import Programador,Music



admin.site.register(Programador)

admin.site.register(Music)