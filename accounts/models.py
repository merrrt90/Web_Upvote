from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin)
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from django.core.validators import MinLengthValidator


class UserManager(BaseUserManager):
    def _create_user(self, email, password, is_staff, is_superuser):
        now = timezone.now()
        if not email:
            raise ValueError('users must have an email address')
        email = self.normalize_email(email)
        user = self.model(email=email,
                          is_staff=is_staff,
                          is_superuser=is_superuser,
                          last_login=now,
                          date_joined=now,
                          avatar='/static/assets/images/person-male.png',
                          product_limit=5,
                          first_name=None,
                          last_name=None)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None):
        user = self._create_user(email, password, False, False)
        return user

    def create_superuser(self, email, password):
        user = self._create_user(email, password, True, True)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    """My own custom user class"""

    email = models.EmailField(
        max_length=255, unique=True, db_index=True, verbose_name=_('email address'))
    date_joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    avatar = models.ImageField(upload_to='avatar/', blank=True, null=True)
    product_limit = models.IntegerField(default=5)
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    username = models.CharField(max_length=100, unique=True, validators=[
                                MinLengthValidator(4)])

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email


'''from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    avatar = models.ImageField(upload_to='avatar/', blank=True, null=True)
    product_limit = models.IntegerField(default=5)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)'''
