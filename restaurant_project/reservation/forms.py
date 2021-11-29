from django import forms
from .models import Reservation



class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = "__all__"
        widgets = {
            "name": forms.TextInput(attrs={
                "class": "form-control"
                }),

            "email": forms.EmailInput(attrs={
                "class": "form-control"
                }),
            "phone": forms.NumberInput(attrs={
                "class": "form-control"
                }),
            "number_of_person": forms.NumberInput(attrs={
                "class": "form-control"
                }),

            "date": forms.DateInput(attrs={
                "class": "form-control"
                }),

            "time": forms.TimeInput(attrs={
                "class": "form-control"
                }),
        }

