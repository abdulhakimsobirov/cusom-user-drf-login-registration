from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    def create(self, email, password, **extra_field):

        if not email:
            raise ValueError('email must be set.')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_field)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_field):
        extra_field.setdefault('is_active', True)
        extra_field.setdefault('is_staff', True)
        extra_field.setdefault('is_superuser', True)
        return self.create(email, password, **extra_field)
