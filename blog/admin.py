from django.contrib import admin

from blog import models
# Register your models here.
@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title','status','owner','created_time']
    list_filter = ['title','status','owner']

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Tag)
class TagAdmin(admin.ModelAdmin):
    pass


