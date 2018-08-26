from django.shortcuts import render, redirect


def welcome(request):
    if request.user.is_authenticated:
        return redirect('hotel_home')
    else:
        return render(request, 'booking/welcome.html')
