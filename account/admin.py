from django.contrib import admin
from account.models import Account
from django.contrib import admin
# Register your models here.

@admin.register(Account)
class Account(admin.ModelAdmin):
    ordering = ['date_joined']
    search_fields = ['username', 'email']
    list_display = ['username', 'email', 'date_joined', 'is_staff']
    readonly_fields = ['date_joined', 'last_login']

# admin.site.register(Account)
