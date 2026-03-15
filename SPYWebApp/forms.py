from django import forms

class form_1(forms.Form):
    amb_temp=forms.IntegerField(label='amb')
    mod_temp=forms.IntegerField(label='mod')
    time=forms.IntegerField(label='time')
    irradiation=forms.DecimalField(label='irr')

class form_2(forms.Form):
    date = forms.DateInput()
    location = forms.CharField(label='loca', max_length=100)
    time = forms.TimeInput()