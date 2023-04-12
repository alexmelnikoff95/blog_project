from django.contrib import admin

from blog.models import Post, Tag

admin.site.register(Tag)


@admin.register(Post)
class AdminPost(admin.ModelAdmin):
    list_display = [field.name for field in Post._meta.get_fields() if not field.many_to_many]




