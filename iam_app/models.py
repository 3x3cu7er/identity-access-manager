from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission,User

class CustomUser(AbstractUser):
    groups = models.ManyToManyField(
        Group,
        related_name='custom_user_set',  # Unique related name
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_user_set',  # Unique related name
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

class UserProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.user.username

from django.db import models
from django.conf import settings

class AccessRule(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    target_user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='target_user', on_delete=models.CASCADE)
    can_access = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user} -> {self.target_user}: {self.can_access}"


class IdentityInfo(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    bio = models.TextField(blank=True)
    allowed_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='allowed_identity_infos', blank=True)

    def __str__(self):
        return self.name