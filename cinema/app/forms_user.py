from django import forms

class BookingForm(forms.Form):
    fullname = forms.CharField(label='Họ và tên')
    phone = forms.CharField(label='Số điện thoại')
    qty = forms.IntegerField()
    date = forms.DateTimeField(input_formats=['%d/%m/%Y %H:%M'])
