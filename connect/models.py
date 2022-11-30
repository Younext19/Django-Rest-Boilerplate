from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
import uuid
# Create your models here.


class User(AbstractUser):
    uid = models.UUIDField(unique=True, editable=False,
                           default=uuid.uuid4, verbose_name='Public identifier')

    username = models.CharField(
        max_length=150, unique=True)

    email = models.EmailField(
        _('email address'), unique=True, blank=True, null=True, default=None)

    phone_number = models.CharField(
        max_length=17, unique=True, blank=True, null=True)

    fix = models.CharField(
        max_length=17, unique=True, blank=True, null=True)

    isconfirmed = models.BooleanField(_('Is Confirmed'), default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.username

# LOCATION INFO CLASS AND ADD USER AS FOREIGN KEY


class AddressUser(models.Model):
    street = models.CharField(max_length=255, blank=True)
    street2 = models.CharField(max_length=255, blank=True)





class Country(models.Model):

    country_name = models.CharField(max_length=255, unique=True)

    country_iso = models.CharField(max_length=3)

    class Meta:
        verbose_name_plural = 'countries'
        ordering = ['country_name']

    def __str__(self):
        return self.country_name



class State(models.Model):

    name = models.CharField(max_length=255)

    code = models.CharField(max_length=50)

    country = models.ForeignKey(
        Country, related_name="states", on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'states'
        ordering = ['name']

    def __str__(self):
        return ("%s - %s") % (self.code, self.name)


class City(models.Model):
    state = models.ForeignKey(
        State, related_name='cities', on_delete=models.SET_NULL, null=True)

    zip_code = models.CharField(max_length=50)

    name = models.CharField(max_length=255)

    longitude = models.FloatField()

    latitude = models.FloatField()

    class Meta:
        verbose_name_plural = 'cities'
        ordering = ['name']

    def __str__(self):
        return ("%s - %s - %s") % (self.state.name, self.name, self.zip_code)
