from django import forms
from .models import usermodel
class userform(forms.ModelForm):
    class Meta:
        model =  usermodel
        fields ='__all__'