from django.contrib import admin

from .models import UserOS, Gate


class UserOSAdmin(admin.ModelAdmin):
    list_display = ('pk', 'login', 'add_date', 'num_pass', 'is_working',)
    list_display_links = ('pk', 'login',)
    list_editable = ('is_working',)
    search_fields = ('login',)
    list_filter = ('is_working',)
    empty_value_display = '-пусто-'


class GateAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title',)
    list_display_links = ('pk', 'title',)
    search_fields = ('title',)
    empty_value_display = '-пусто-'


admin.site.register(UserOS, UserOSAdmin)
admin.site.register(Gate, GateAdmin)
