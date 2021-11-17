# Django
from django.db import models
from django.contrib.auth.models  import AbstractBaseUser
from django.contrib.auth.models  import PermissionsMixin
from django.contrib.auth.models  import BaseUserManager
from django.contrib.auth.hashers import make_password

class UserProfileManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, phone_number, address,  password = None):
        if not email:
            raise ValueError("Users must have an email")

        email = self.normalize_email(email)
        user = self.model(
            email = email,
            first_name = first_name,
            last_name = last_name,
            phone_number = phone_number,
            address = address
        )

        user.set_password(password)
        user.save(using = self._db)

    def create_user(self, email, first_name, last_name, phone_number, address,  password):
        user = self.create_user(
            email,
            first_name,
            last_name,
            phone_number,
            address,
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

    first_name = models.CharField(
        "Fist Name",
        max_length = 256,
        blank = True
    )

    last_name = models.CharField(
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

    def save(self, **kwargs):
        some_salt = 'mMUj0DrIK6vgtdIYepkIxN'
        self.password = make_password(self.password, some_salt)
        super().save(**kwargs)

    USERNAME_FIELD = "email"
