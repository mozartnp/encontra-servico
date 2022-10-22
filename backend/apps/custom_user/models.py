import uuid

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils.translation import gettext_lazy as _

class CustomUserManager(BaseUserManager):
    '''
    Class to create a user
    '''
    def create_user(self, username, is_client, password=None):
        if not username:
            raise ValueError("Username is required.")
        if not is_client:
            raise ValueError("is_client is required.")

        user = self.model(
            username = username,
            collaborator = collaborator,
            is_client = is_client,
        )

        user.set_password(password)

        user.save(using=self._db)
        return user

    def create_superuser(self, username, password, is_client):
        if not username:
            raise ValueError("Username is required.")
        if not is_client:
            raise ValueError("is_client is required.")

        user = self.model(
            username = username,
            password = password,
            is_client = is_client,
        )

        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.set_password(password)

        user.save(using=self._db)
        return user

class CustomUser(AbstractBaseUser):
    '''
    Model to create a custom user on django
    '''
    id_user = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=254, unique=True)
    is_client = models.BooleanField(help_text="If true is a client, if false is a company")

    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['is_client',]

    objects = CustomUserManager()

    def __str__(self):
        return self.username
    
    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True