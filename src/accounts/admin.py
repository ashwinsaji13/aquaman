from django.contrib import admin
#from .models import Account
# # Register your models here.
from django.contrib.auth import get_user_model

#admin.site.register(Account)
# @admin.register(Account)
# class AccountAdmin(admin.ModelAdmin):
#     exclude = (
#                 # 'password',
#                 'is_admin',
#                 'color'
#                 )
#     readonly_fields = ('last_login',)

#     def save_model(self, request, user, form, change):
#         if user.password and len(user.password) < 30:
#             user.set_password(user.password)
#         user.save()

User = get_user_model()
admin.site.register(User)
