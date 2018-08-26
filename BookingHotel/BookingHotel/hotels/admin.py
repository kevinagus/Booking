# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import Hotel,Room

admin.site.register(Hotel)
admin.site.register(Room)

