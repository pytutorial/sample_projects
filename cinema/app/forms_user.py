from django import forms

class BookingForm(forms.Form):
    fullname = forms.CharField()
    phone = forms.CharField()
    room = forms.CharField()
    selectedSeats = forms.CharField()
    date = forms.CharField()
