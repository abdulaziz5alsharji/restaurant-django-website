from django.shortcuts import render
from .forms import ReservationForm
# Create your views here.

def reserve_table(request):
    if request.method == "POST":
        form = ReservationForm(request.POST or None)
        if form.is_valid():
            form.save()
        else:
            return render(request, "reservation/reservation.html", context={
                "form": form
            })
    return render(request, "reservation/reservation.html", context={
        "form": ReservationForm()
    })