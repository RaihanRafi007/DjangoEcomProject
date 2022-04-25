from django.db import models
from django.conf import settings
from django.db.models.base import Model
from django.db.models.expressions import Value

# Create your models here.

class BillingAddress(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    address = models.CharField(max_length=264, blank=True)
    zipcode = models.CharField(max_length=10, blank=True)
    city = models.CharField(max_length=30, blank=True)
    country = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return f'{self.user.profile.username} billing address'

    def is_fully_filled(self):
        field_names = [f.name for f in self._meta.get_fields()]

        for field_name in field_names:
            Value = getattr(self, field_name)
            if Value is None or Value=='':
                return False
        return True

    class Meta:
        verbose_name_plural = 'Billing Address'