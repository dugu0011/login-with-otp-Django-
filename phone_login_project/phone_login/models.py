from django.db import models

# Create your models here.


from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class PhoneNumbers(models.Model):
    phone_number = PhoneNumberField(unique=True)
    otp = models.CharField(max_length=6)
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return str(self.phone_number)
