from django.contrib import admin
from django.utils.timezone import now
from esiomotores.contacts.models import Contact

class ContactModelAdmin(admin.ModelAdmin):
    search_fields = ('name', 'email', 'phone', 'ipaddr', 'created_at')
    list_display = ('name', 'email', 'phone', 'ipaddr', 'created_at', 'sent_today')
    date_hierarchy = 'created_at'
    list_filter = ('created_at',)

    def sent_today(self, obj):
        return obj.created_at.date() == now().date()

    sent_today.short_description = 'enviada hoje?'
    sent_today.boolean = 'True'


admin.site.register(Contact, ContactModelAdmin)
