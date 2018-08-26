# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible

from django.db import models
from django.contrib.auth.models import User


class HotelQuerySet(models.QuerySet):
    def hotels_for_keeper(self, user):
        return self.filter(hotelKeeper=user)


@python_2_unicode_compatible
class Hotel(models.Model):
    hotelKeeper = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    descriptions = models.CharField(max_length=2000)
    city = models.CharField(max_length=50)
    address = models.CharField(max_length=100)

    object = HotelQuerySet.as_manager()

    def __str__(self):
        return "{0}".format(self.name)


class Room(models.Model):
    number = models.IntegerField
    beds = models.IntegerField
    service = models.CharField(max_length=500)
    price = models.FloatField
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)


