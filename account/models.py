from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class MyAccountManager(BaseUserManager):
    def create_user(self, email, phone_number, name, date_of_birth, national_id, password=None):
        if not email:
            raise ValueError('User must have an email')
        if not phone_number:
            raise ValueError('User must have a phone number')
        if not name:
            raise ValueError('User must have a name')
        if not date_of_birth:
            raise ValueError('User must have a date of birth')
        if not national_id:
            raise ValueError('User must have a national id')

        user = self.model(
            email=self.normalize_email(email),
            phone_number=phone_number,
            name=name,
            date_of_birth=date_of_birth,
            national_id=national_id,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, phone_number, name, date_of_birth, national_id, password):
        user = self.create_user(
            email=self.normalize_email(email),
            phone_number=phone_number,
            name=name,
            date_of_birth=date_of_birth,
            national_id=national_id,
            password=password
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser):
    email = models.EmailField(verbose_name='email', max_length=64, unique=True)
    username = models.CharField(max_length=64, blank=True)
    date_joined = models.DateTimeField(
        verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    phone_number = models.CharField(verbose_name='phone number', max_length=16)
    name = models.CharField(verbose_name='name', max_length=128)
    date_of_birth = models.DateField(
        verbose_name='date of birth', auto_now=False)
    national_id = models.CharField(verbose_name='national id', max_length=10)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phone_number', 'name', 'date_of_birth', 'national_id']

    objects = MyAccountManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True
