from django.contrib import admin
from .models import Account
from django.contrib.auth.models import Group
# # Register your models here.
from django.contrib.auth import get_user_model

# admin.site.register(Account)
admin.site.unregister(Group)


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    # exclude = (
    #     'password',
    #     'admin'
    # )
    # readonly_fields = ('last_login',)

    def save_model(self, request, user, form, change):
        print(user)
        if user.password and len(user.password) < 30:
            user.set_password(user.password)
        user.save()

# User = get_user_model()
# admin.site.register(User)
