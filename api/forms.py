from django import forms

class ValveForm(forms.Form):
    
    open_input = forms.CharField(widget=forms.fields.TextInput(attrs={'id': 'id-open-input'}))
    min_temp = forms.CharField(widget=forms.fields.TextInput(attrs={'id': 'id-min-temp-input'}))
    max_temp = forms.CharField(widget=forms.fields.TextInput(attrs={'id': 'id-max-temp-input'}))