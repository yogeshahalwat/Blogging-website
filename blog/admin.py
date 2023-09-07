from django.contrib import admin
from .models import PostModel,comment


# Register your models here.


class PostModelAdmin(admin.ModelAdmin):
    list_display=("title","publication_date")

admin.site.register(PostModel,PostModelAdmin)
admin.site.register(comment)