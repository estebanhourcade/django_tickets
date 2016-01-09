from django.contrib import admin
from tickets.models import Ticket

# Register your models here.
class TicketAdmin(admin.ModelAdmin):
	list_display = ('title','author','created_date', 'status')
	list_filter = ('created_date','title', 'author', 'assignee')
	
admin.site.register(Ticket, TicketAdmin)
