from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models


def upload_profile_pics_location(instance, filename):
    file_path = f'Profile Pics/{instance.user.username}/{filename}'
    return file_path


class UserManager(BaseUserManager):

    def create_user(self, email, username, password=None):

        if not email:
            raise ValueError('Invalid email')
        if not username:
            raise ValueError('Invalid username')

        user = self.model(
            email=self.normalize_email(email),
            username=username
        )

        user.set_password(password)

        user.save(using=self._db)

        return user

    def create_superuser(self, email, username, password):

        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password
        )

        user.is_staff = True
        user.is_admin = True
        user.is_superuser = True

        user.save(using=self._db)

        return user


class User(AbstractBaseUser):

    email = models.EmailField(unique=True, max_length=100)
    username = models.CharField(unique=True, max_length=100)
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)

    objects = UserManager()
    REQUIRED_FIELDS = ['username', 'password']
    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email

    def has_perm(self, perms, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True


class ProfileImage(models.Model):
    profile_picture = models.ImageField(
        upload_to=upload_profile_pics_location, default='default_profile_picture.jpg')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.profile_picture.name
