from django import forms
from .models import User_Address

class AddressForm(forms.ModelForm):
    class Meta:
        model = User_Address
        fields = ['house_name', 'landmark','city',  'pincode', 'district', 'state','country']
    
    def __init__(self, *args, **kwargs):
        super(AddressForm, self).__init__(*args, **kwargs )
        self.fields['house_name'].widget.attrs['placeholder'] = 'Enter First name'
        self.fields['landmark'].widget.attrs['placeholder'] = 'Enter Last name'
        self.fields['city'].widget.attrs['placeholder'] = 'Enter Email address'
        self.fields['pincode'].widget.attrs['placeholder'] = 'Enter Phone number'
        self.fields['district'].widget.attrs['placeholder'] = 'Enter Phone number'
        self.fields['state'].widget.attrs['placeholder'] = 'Enter Phone number'
        self.fields['country'].widget.attrs['placeholder'] = 'Enter Phone number'
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control form-control-md w-100'