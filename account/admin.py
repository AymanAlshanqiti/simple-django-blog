from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from account.models import Account


class AccountAdmin(UserAdmin):
    list_display = ['email', 'name', 'phone_number', 'date_of_birth',
                    'last_login', 'is_active', 'is_admin', 'is_staff']
    search_fields = ['email', 'name', 'phone_number', 'national_id']
    readonly_fields = ['date_joined', 'last_login']

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(Account, AccountAdmin)
