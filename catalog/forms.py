from django import forms 
class RentForm(forms.Form):
    rent_duration = forms.ChoiceField(choices=['1 month', '2 months'])
