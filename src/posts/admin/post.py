from django.contrib import admin


class PostAdmin(admin.ModelAdmin):
    search_fields = [
        'title',
        'body',
    ]
    list_display = [
        'author',
        'title',
        'created_at',
        'updated_at',
    ]
    list_filter = [
        'author',
    ]
