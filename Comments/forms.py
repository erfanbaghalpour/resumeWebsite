from django import forms
from django_recaptcha.fields import ReCaptchaField
from .models import Comment


class CommentForm(forms.Form):
    name = forms.CharField(required=True, label='ّFullname', max_length=300,
                           error_messages={'required': 'Please enter your fullname',
                                           'max_length': 'It could not be more than 300'},
                           widget=forms.TextInput(attrs={'class': 'form-control form-control-lg text-light my-class',
                                                         'placeholder': 'ّFullname',
                                                         'id': 'contactForm'}))
    email = forms.EmailField(required=True, label='Email', max_length=300,
                             widget=forms.EmailInput(attrs={'class': 'form-control form-control-lg text-light',
                                                            'placeholder': 'Email', 'id': 'contactForm'}),
                             error_messages={'required': 'Please enter your email'})
    text = forms.CharField(required=True, label='Text', max_length=2000,
                           widget=forms.Textarea(attrs={'class': 'form-control form-control-lg text-light my-class',
                                                        'placeholder': 'Text', 'id': 'contactForm'}),
                           error_messages={'required': 'Please enter your text',
                                           'max_length': 'It could not be more than 2000'})
    captcha = ReCaptchaField()


# class ReplyForm(forms.Form):
#     name = forms.CharField(required=True, label='ّFullname', max_length=300,
#                            error_messages={'required': 'Please enter your fullname',
#                                            'max_length': 'It could not be more than 300'},
#                            widget=forms.TextInput(attrs={'class': 'form-control form-control-lg text-light my-class',
#                                                          'placeholder': 'ّFullname',
#                                                          'id': 'contactForm'}))
#     email = forms.EmailField(required=True, label='Email', max_length=300,
#                              widget=forms.EmailInput(attrs={'class': 'form-control form-control-lg text-light',
#                                                             'placeholder': 'Email', 'id': 'contactForm'}),
#                              error_messages={'required': 'Please enter your email'})
#     re_comment = forms.CharField(required=True, label='Text', max_length=2000,
#                                  widget=forms.Textarea(
#                                      attrs={'class': 'form-control form-control-lg text-light my-class',
#                                             'placeholder': 'Text', 'id': 'contactForm'}),
#                                  error_messages={'required': 'Please enter your text',
#                                                  'max_length': 'It could not be more than 2000'})


class CommentFormNew(forms.ModelForm):
    captcha = ReCaptchaField()

    class Meta:
        model = Comment
        fields = {
            'blog',
            'name',
            'text',
            'email',
        }
