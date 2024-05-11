from django.contrib import admin
from .models import *


class ClientsModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email', 'passport']
    list_display_links = ['passport']
    search_fields = ['first_name', 'last_name', 'email', 'passport']
    list_filter = ['first_name', 'last_name', 'email', 'passport']
    list_editable = ['first_name', 'last_name', 'email']

    class Meta:
        model = Clients


class InsuranceObjectModelAdmin(admin.ModelAdmin):
    list_display = ['object_name', 'description']
    list_display_links = ['object_name']
    search_fields = ['object_name']
    list_filter = ['object_name']
    list_editable = ['description']

    class Meta:
        model = InsuranceObject


class ContractsModelAdmin(admin.ModelAdmin):
    list_display = ['client_id', 'object_id', 'contract_date', 'insurance_payment']
    list_display_links = ['client_id', 'object_id', 'contract_date']
    search_fields = ['client_id', 'object_id', 'contract_date', 'insurance_payment']
    list_filter = ['client_id', 'object_id', 'contract_date', 'insurance_payment']
    list_editable = ['insurance_payment']

    class Meta:
        model = Contracts


class InsurancePaymentsModelAdmin(admin.ModelAdmin):
    list_display = ['contract_id', 'date']
    search_fields = ['contract_id', 'date']
    list_filter = ['contract_id', 'date']


admin.site.register(Clients, ClientsModelAdmin)
admin.site.register(InsuranceObject, InsuranceObjectModelAdmin)
admin.site.register(Contracts, ContractsModelAdmin)
admin.site.register(InsurancePayments, InsurancePaymentsModelAdmin)
