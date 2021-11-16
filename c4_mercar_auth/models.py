from django.db import models

from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin

from django.contrib.auth.models import BaseUserManager

class UserProfileManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, phone_number, password = None):
        if not email:
            raise ValueError("Users must have an email")

        email = self.normalize_email(email)
        user = self.model(
            email = email,
            first_name = first,
            last_name = last_name,
            phone_number = phone_number,
        )

        user.set_password(password)
        user.save(using = self._db)

    def create_user(self, email, first_name, last_name, phone_number, password):
        user = self.create_user(
            email,
            first_name,
            last_name,
            phone_number,
            password
        )
        user.is_superuser = True
        user.is_staff = True
        user.save(using = self._db)

class UserProfile(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        "Email",
        max_length = 320,
        unique = True,
    )

    fist_name = models.CharField(
        "Fist Name",
        max_length = 256,
        blank = True
    )

    last_Name = models.CharField(
        "Last Name",
        max_length = 256,
        blank = True
    )

    phone_number = models.CharField(
        "Phone Number",
        max_length = 10,
        blank = True
    )

    address = models.CharField(
        "Address",
        max_length = 256,
        blank = True
    )

    objects = UserProfileManager()

    USERNAME_FIELD = "email"
