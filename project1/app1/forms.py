
from django.core.exceptions import ValidationError
from django import forms
from app1.models import UserModel


class user_form(forms.ModelForm, forms.Form):
    password2 = forms.CharField(label="Conform Password",required = False)
    class Meta:
        model = UserModel
        fields = ['email', 'name', 'password']
        labels = {
            'email': 'Enter Email:',
            'name':'Enter Name',
            'password':'Enter Password'
        }
    
    def clean_name(self):
        name = self.cleaned_data.get('name')

        if not name:
            raise ValidationError("Please Enter Name", code="empty_feild_error")
        if len(name) >= 20:
            raise ValidationError("Please Enter Name of 20 Character", code="invalid_name_error")
        return name
    def clean_email(self):
        email = self.cleaned_data.get('email')

        if not email:
            raise ValidationError("Plese Enter Email", code="empty_feild_error")
        return email
    def clean_password(self):  
        password = self.cleaned_data.get('password')     
        password2 = self['password2'].value()     
        if password and password2:
            if password != password2:  
                raise ValidationError("Password doesn't match", code='password_not_match')
            else:
                return password
        else:
            raise ValidationError("Please Enter Passwords", code='empty_feild_error')