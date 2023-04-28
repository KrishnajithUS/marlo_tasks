from django.db import models
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser,PermissionsMixin)


class MyUserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, password=None, **kwargs):
        if not email:
            raise ValueError('User must have an email')
        user = self.model(email=self.normalize_email(email), first_name=first_name, last_name=last_name, **kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, last_name, password=None, **kwargs):
        user = self.create_user(email, first_name, last_name, password, **kwargs)
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)


class MyUser(AbstractBaseUser, PermissionsMixin):
    USER = 1
    MANAGER = 2
    EMPLOYEE = 3
    ROLE_CHOICES = (
        (USER, 'Admin'),
        (MANAGER, 'Manager'),
        (EMPLOYEE, 'Employee')
    )
    email = models.EmailField(verbose_name='email address', max_length=255, unique=True)
    first_name = models.CharField(max_length=300)
    last_name = models.CharField(max_length=200)
    confirm_password = models.CharField(max_length=100)
    role = models.PositiveIntegerField(choices=ROLE_CHOICES, default=1, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perm(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin
