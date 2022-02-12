from django.contrib import admin
from.models import list2

class listAdmin2(admin.ModelAdmin):
    list_display = ('name','email','phone','age')

# Register your models here.
admin.site.register(list2)




