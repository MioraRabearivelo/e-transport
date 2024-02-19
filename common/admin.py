

from django.contrib import admin
from .models import CustomerUser

class CustomerUserAdmin(admin.ModelAdmin):
    model = CustomerUser
    ordering = ('first_phone_number',)
    search_fields = ('customer_name',)
    list_display = [
        'first_phone_number', 'second_phone_number',
        'customer_name',
    ]

admin.site.register(CustomerUser, CustomerUserAdmin)