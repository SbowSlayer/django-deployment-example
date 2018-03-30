from django import forms
from revision_app.models import RevisionUsers
from django.contrib.auth.models import User


class RevisionUsersForm (forms.ModelForm):
    
    password = forms.CharField(widget = forms.PasswordInput()) #this will start hashing the password
    
    class Meta:
        model = User
        fields = ('username','email','password')
        
        
class RevisionUsersExtra (forms.ModelForm):
    
    class Meta:
        model = RevisionUsers
        fields = ('behance_folio','profile_pic')
        
        
