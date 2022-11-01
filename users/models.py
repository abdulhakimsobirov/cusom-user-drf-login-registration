# from django.db import models
# from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
# from django.utils import timezone
# from .manager import UserManager

# class CustomUser(AbstractBaseUser,PermissionsMixin):
#     email = models.EmailField(verbose_name="email address",unique=True)
#     is_staff = models.BooleanField(default=False)
#     is_active = models.BooleanField(default=True)
#     date_joined = models.DateTimeField(default=timezone.now)
    
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = []
    
#     objects = UserManager()
    
#     class Meta:
#         verbose_name='User'
    
#     def __str__(self):
#         return self.email


from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin


class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""
    use_in_migrations = True

    def _create_user(self, language, password, **extra_fields):
        """Create and save a User with the given phone and password."""
        if not language:
            raise ValueError('The given phone must be set')
        user = self.model(language=language, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, language, password=None, **extra_fields):
        """Create and save a regular User with the given phone and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(language, password, **extra_fields)

    def create_superuser(self, language, password, **extra_fields):
        """Create and save a SuperUser with the given phone and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self._create_user(language, password, **extra_fields)


class User(AbstractUser, PermissionsMixin):
    username = models.CharField(max_length=100, unique=True, null=True, blank=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    title = models.CharField(max_length=100, null=True)
    language = models.CharField(max_length=13, unique=True)
    description = models.CharField(max_length=255)
    avatar = models.ImageField(upload_to='user_images/', blank=True, null=True)
    location = models.CharField(max_length=255)




    objects = UserManager()

    USERNAME_FIELD = 'language'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'{self.last_name}  {self.first_name}'