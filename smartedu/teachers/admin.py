from django.contrib import admin
from .models import Teacher

@admin.register(Teacher)
class Admin(admin.ModelAdmin):
    list_display = ('name','title',)
    search_fields = ('name',)

