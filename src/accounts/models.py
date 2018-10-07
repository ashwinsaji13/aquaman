from django.db import models
from django.conf import settings

# ----for auth tokens---------------------------------------------------------------
from django.dispatch import receiver
from django.db.models.signals import post_save
# -----------------------------------------------------------------------------------
from django.contrib.auth.models import AbstractBaseUser

# ---for validating the models field--------------------------------------------------
from django.core.validators import RegexValidator, MinLengthValidator
# -------------------------------------------------------------------------------------

# ------------rest-framework------------------------------------------------------------
from rest_framework.authtoken.models import Token
# --------------------------------------------------------------------------------------

# import from src.accounts.managers
from .managers import AccountManager


class Account(AbstractBaseUser):
        """
        Custom Auth User model.
        Provides all the basic features of Django's auth User model, plus some
        required custom functionalities.
        """
        # for validating the phone number
        phone_number_regex_validator = RegexValidator(regex=r'^[0-9]{10}$', message='Invalid Phone Number.')

        # custom fields for USER registration
        email = models.EmailField(unique=True)
        full_name = models.CharField(max_length=64)
        phone_number = models.CharField(max_length=10, validators=[phone_number_regex_validator,\
                                                                   MinLengthValidator(10)])
        address = models.CharField(max_length=128, default='HOME-TOWN')

        active = models.BooleanField(default=True)
        admin = models.BooleanField(default=False)
        staff = models.BooleanField(default=False)
        superuser = models.BooleanField(default=False)
        initial_login = models.BooleanField(default=True)

        objects = AccountManager()

        USERNAME_FIELD = 'email'

        class Meta:
            ordering = ('-id', )

        def __str__(self):
            return self.email

        @property
        def get_full_name(self):
            return self.get_full_name

        def get_short_name(self):
            return self.email

        def has_module_perms(self, temp):
            return True

        def has_perm(self, temp):
            return True

        @property
        def is_active(self):
            return self.active

        @property
        def is_admin(self):
            return self.admin

        @property
        def is_staff(self):
            return self.staff


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    """
    Create auth token whenever a user is created.
    """
    if created:
        Token.objects.create(user=instance)
