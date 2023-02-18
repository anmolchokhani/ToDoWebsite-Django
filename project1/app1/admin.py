from django.contrib import admin
from .models import ToDo

# Register your models here.
@admin.register(ToDo)
class ToDoAdmin(admin.ModelAdmin):
    list_display= [ field.name for field in ToDo._meta.get_fields()]

    