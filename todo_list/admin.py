from django.contrib import admin
from .models import Category, Todo
# Register your models here.


class TodoAdmin(admin.ModelAdmin):
    """
    admin用にカスタマイズ
    """

    list_display = ('title', 'dead_line')
    search_fields = ['title']

    fieldsets = (
        (None, {
            "fields": [
                'title', 'category'
            ],
        }),
        ('Date information', {
            "fields": [
                'dead_line'
            ]
        })
    )


admin.site.register(Category)
admin.site.register(Todo, TodoAdmin)
