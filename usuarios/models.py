from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
# Create your models here.
# Modelos que define o DB da aplicacao

class UsuarioManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("E necessario digitar o email.")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError("Os super utilizadores devem ter o campo is_staff=True")
        if extra_fields.get('is_superuser') is not True:
            raise ValueError("Os super utilizadores devem ter o campo is_superuser=True")
        return self.create_user(email, password, **extra_fields)
          

class Usuario(AbstractUser):
    username = None
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UsuarioManager()

    def __str__(self):
        return self.email
    