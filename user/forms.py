from django import forms
from django.contrib.auth.models import User 

class AuthUserForm(forms.ModelForm):
    password_confirm = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields =['username','first_name','last_name','gender','dob','email','password',"password_confirm"]

    def clean(self):
        clean_data = super().clean()
        repeat_password = clean_data.get("password_confirm")
        password = clean_data.get("password")

        if password and repeat_password and password != repeat_password:
            forms.ValidationError("passwords do not match")


