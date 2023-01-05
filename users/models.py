from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.

class TimeStamp(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        
class UserManager(BaseUserManager):
    def create_user(self, email, name, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            name=name,
        )

        user.set_password(password)
        user.is_active = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, password=None):
        user = self.create_user(
            email=email,
            password=password,
            name=name,
        )

        user.is_admin = True
        user.save(using=self._db)
        return         
        
class User(AbstractBaseUser, TimeStamp):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=50, unique=True)

    objects =  UserManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELD = [
        'name',
    ]
    
    def __str__(self):
        return f'{self.name}({self.email})'

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return self.is_admin

    class Meta:
        db_table = 'users'