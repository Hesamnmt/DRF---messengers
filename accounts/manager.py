from django.contrib.auth.models import BaseUserManager


class UserManger(BaseUserManager):

    def create_user(self, phone_number, first_name, last_name, info):

        if not phone_number:
            raise ValueError('User Must Have PHONE_NUMBER')

        if not first_name:
            raise ValueError('User Must Have FIRST_NAME')

        if not last_name:
            raise ValueError('User Must Have LAST_NAME')

        if not info:
            raise ValueError('User Must Have INFORMATION')

        user = self.model(phone_number=phone_number, first_name=first_name, last_name=last_name, info=info)
        user.save(using=self._db)
        return user

