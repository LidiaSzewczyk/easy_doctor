from django.contrib import admin

from .models import CustomUser


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_full_name', 'username')
    search_fields = ('first_name', 'last_name',)
    list_display_links = ('id', 'get_full_name')
    save_on_top = True


admin.site.register(CustomUser, CustomUserAdmin)
