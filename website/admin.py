from django.contrib import admin
from website.models import Employees


class EmployeesAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'ident_id', 'contribution_time', 'remuneration')
    search_fields = ('name', 'ident_id', 'remuneration')

admin.site.register(Employees, EmployeesAdmin)