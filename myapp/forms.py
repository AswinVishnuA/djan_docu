from django import forms

class pinForm(forms.Form):
    Distance_from_left=forms.FloatField()

class lobForm(forms.Form):    
    Distance =forms.FloatField(min_value=0)
    
class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)



class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)    