from django import forms


class ContactUsForm(forms.Form):
    name = forms.CharField(max_length=200)
    subject = forms.CharField(max_length=300)
    email = forms.EmailField()
    text = forms.CharField(widget=forms.Textarea())
