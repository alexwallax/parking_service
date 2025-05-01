from django.contrib import admin

from customers.models import Customer


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['name', 'cpf', 'phone', 'created_at'] # campos que vão aparecer
    search_fields = ['name', 'cpf', 'phone'] # campos qu podem ser filtrados
