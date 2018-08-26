# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.decorators import login_required
from django.shortcuts import render , redirect

from .models import Hotel


@login_required
def home(request):
    hotels_list = Hotel.object.hotels_for_keeper(request.user)
    return render(request, "hotel/hotels.html", {'hotels_list': hotels_list})
