import sqlite3
from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
  
    first_name = models.CharField(max_length=240)
    last_name = models.CharField(max_length=240)
    address = models.CharField(max_length=240)
    city = models.CharField(max_length=55)
    state_province = models.CharField(max_length=55)
    country = models.CharField(max_length=55)
    postal_code = models.CharField(max_length=9)
    email = models.EmailField(max_length=55)
    user = models.OneToOneField(User)

    class Meta:
        verbose_name_plural = "Customer"

    def __str__(self):
        return '{} {} {} {} {} {} {} {} {} {}'.format(self.first_name, self.last_name, self.address, self.city, self.state_province, self.country, self.postal_code, self.email, self.user.username , self.user.password)

    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name

    def get_address(self):
        return self.address

    def get_city(self):
        return self.city

    def get_state_province(self):
        return self.state_province

    def get_country(self):
        return self.country

    def get_postal_code(self):
        return self.postal_code

    def get_email(self):
        return self.email

    def get_password(self):
        return self.user.password

    def get_full_name(self):
        full_name = self.first_name + " " + self.last_name
        return full_name