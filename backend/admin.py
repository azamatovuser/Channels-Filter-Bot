from django.contrib import admin
from .models import Group, Person, Link
from .actions import export_as_xls


class PersonAdmin(admin.ModelAdmin):
    list_display = ['id', 'full_name']
    actions = [export_as_xls]


admin.site.register(Link)


admin.site.register(Person, PersonAdmin)


admin.site.register(Group)