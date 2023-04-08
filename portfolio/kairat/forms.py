from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label='Имя', max_length=255, widget=forms.TextInput(attrs={"placeholder": "Name"}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={"placeholder": "Email"}))
    content = forms.CharField(widget=forms.Textarea(attrs={"placeholder": "Message"}))