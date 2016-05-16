from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
import datetime, time


class NewUserManager(BaseUserManager):
    def create_user(self, username, age, sex, password):
        if not username:
            raise ValueError('Users must define a username')
        user = self.model(
            username=username,
            age=age,
            sex=sex
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, age, sex, password):
        user = self.model(
            username=username,
            age=age,
            sex=sex
        )
        user.is_admin = True
        user.set_password(password)
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    """
    Custom user class.

    """
    username = models.CharField(max_length=75, unique=True)
    age = models.IntegerField(default=0)
    sex = models.CharField(max_length=1, default='O')

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['age', 'sex']

    objects = NewUserManager()
    def get_full_name(self):
        # The user is identified by their email address
        return self.username

    def get_short_name(self):
        # The user is identified by their email address
        return self.username

    def __str__(self):              # __unicode__ on Python 2
        return self.username

    def has_perm(self, perm, obj=None):

        return True

    def has_module_perms(self, app_label):

        return True

    @property
    def is_staff(self):

        return self.is_admin


class WallPost(models.Model):
    text = models.TextField()
    poster = models.ForeignKey(to=User, related_name='submitted_posts')
    date = models.DateTimeField(default=timezone.now)

    def as_json(self):
        return dict(text=self.text,
                    poster=self.poster.username,
                    date=self.date.strftime("%Y-%m-%d %H:%M:%S"))
