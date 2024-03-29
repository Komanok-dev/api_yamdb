from django.contrib.auth.models import AbstractUser
from django.db import models
from reviews.validators import validate_username


class User(AbstractUser):
    ADMIN = 'admin'
    MODERATOR = 'moderator'
    USER = 'user'
    USER_ROLES = (
        (ADMIN, 'Admin role'),
        (USER, 'User role'),
        (MODERATOR, 'Moderator role'))

    username = models.CharField(
        max_length=150,
        unique=True,
        validators=(validate_username,),
        null=False
    )
    email = models.EmailField(
        max_length=254,
        unique=True,
        null=False)
    role = models.CharField(
        max_length=10,
        choices=USER_ROLES,
        default='user',
    )
    bio = models.TextField(
        'Биография',
        blank=True,
    )

    class Meta:
        ordering = ('username',)

    @property
    def is_admin(self):
        return self.role == self.ADMIN or self.is_superuser

    @property
    def is_moderator(self):
        return self.role == self.MODERATOR

    def __str__(self):
        return self.username
