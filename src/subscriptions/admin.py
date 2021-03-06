from django.contrib import admin
from subscriptions.models import Subscription
import datetime

class SubscriptionAdmin(admin.ModelAdmin):
	list_display = ('name', 'cpf', 'email', 'phone', 'created_at', 'subscribed_today')
	list_filter = ('created_at',)
	date_hierarchy = 'created_at'
	search_fields = ('name', 'email', 'phone', 'created_at')
	
	def subscribed_today(self, obj):
		return obj.created_at.date() == datetime.date.today()
		
	subscribed_today.short_description = u'Inscrito hoje?'
	subscribed_today.boolean = True

admin.site.register(Subscription, SubscriptionAdmin)