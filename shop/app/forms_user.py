from django import forms

class PurchaseForm(forms.Form):
    fullname = forms.CharField(label='Họ và tên')
    phone = forms.CharField(label='Số điện thoại')
    address = forms.CharField(label='Địa chỉ')