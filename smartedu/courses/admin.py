from django.contrib import admin
from . models import Course, Category, Tag

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name','available',)
    list_filter = ('available',)
    search_fields = ('name',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    prepopulated_fields = {'slug':('name',)}


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    prepopulated_fields = {'slug':('name',)}

    

