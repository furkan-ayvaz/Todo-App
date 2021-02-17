from django.contrib import admin
from .models import TODO
# Register your models here.


@admin.register(TODO)
class todoAdmin(admin.ModelAdmin):
    list_display = ["todo_describe","inserted_by","todo_case"]
    list_display_links = ["todo_describe"]
    search_fields = ["todo_describe"]
    list_filter = ["todo_case"]
    class Meta:
        model = TODO
    