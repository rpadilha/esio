from django.contrib import admin
from django.utils.timezone import now
from esiomotores.core.models import CustomerMKT


class CustomerMKTModelAdmin(admin.ModelAdmin):
    search_fields = ('name', 'email')
    list_display = ('name', 'email', 'created_at', 'created_today')
    date_hierarchy = 'created_at'
    list_filter = ('created_at',)

    def created_today(self, obj):
        return obj.created_at.date() == now().date()

    created_today.short_description = 'criado hoje?'
    created_today.boolean = 'True'


admin.site.register(CustomerMKT, CustomerMKTModelAdmin)