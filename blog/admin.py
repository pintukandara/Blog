from django.contrib import admin
from .models import Author,Posts,Tag

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_filter = ("author","tags" ,"date")
    list_display = ("title","author","date")
    prepopulated_fields = {"slug" : ("title",)}

admin.site.register(Author,)
admin.site.register(Posts,PostAdmin)
admin.site.register(Tag)