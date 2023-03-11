from django import forms
from .models import User_Address

class AddressForm(forms.ModelForm):
    class Meta:
        model = User_Address
        fields = ['fullname','contact_number','house_name', 'landmark','city',  'pincode', 'district', 'state','country']
    
    def __init__(self, *args, **kwargs):
        super(AddressForm, self).__init__(*args, **kwargs )
        self.fields['fullname'].widget.attrs['placeholder'] = 'Full Name'
        self.fields['contact_number'].widget.attrs['placeholder'] = 'Mobile'
        self.fields['house_name'].widget.attrs['placeholder'] = 'House Name'
        self.fields['landmark'].widget.attrs['placeholder'] = 'Landmark'
        self.fields['city'].widget.attrs['placeholder'] = 'City'
        self.fields['pincode'].widget.attrs['placeholder'] = 'Pincode'
        self.fields['district'].widget.attrs['placeholder'] = 'District'
        self.fields['state'].widget.attrs['placeholder'] = 'State'
        self.fields['country'].widget.attrs['placeholder'] = 'Country'
        self.fields['country'].widget.attrs['placeholder'] = 'Country'
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control form-control-md w-100'