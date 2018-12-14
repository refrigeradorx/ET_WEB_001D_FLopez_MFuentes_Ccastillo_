from .models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class RegistrarTecnico(UserCreationForm):

    email=forms.EmailField(widget=forms.EmailInput(attrs={'placeholder':'Correo electornico','class':'input-100'},),label="")
    password1=forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Contraseña','class':'input-100'},),label="")
    password2=forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Contraseña','class':'input-100'},),label="")

    class Meta:
        model = User
        fields = ("email", "password1", "password2")
        
    def save(self, commit=True):
        user = super(RegistrarTecnico, self).save(commit=False)
        if commit:
            user.save()
        return user


class LoginForm(AuthenticationForm):
    username=forms.EmailField(widget=forms.EmailInput(attrs={'placeholder':'Correo electronico','class':'form-control'},),label="")
    password=forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Contraseña','class':'form-control'},),label="")


    #class Meta:
    #    model = User
    #    fields = ("email", "password1", "password2")
        
    #def save(self, commit=True):
    #    user = super(RegistrarTecnico, self).save(commit=False)
    #    if commit:
    #        user.save()
    #    return user

    #email=forms.EmailField(widget=forms.EmailInput(attrs={'placeholder':'Correo electornico','class':'input-100'},),label="")
    #password1=forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Contraseña','class':'input-100'},),label="")
    #password2=forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Contraseña','class':'input-100'},),label="")

#class UserCreateForm(UserCreationForm):

    #class Meta:
      #  model = User
      #  fields = ("email", "password1", "password2")

    #def save(self, commit=True):
     #   user = super(UserCreateForm, self).save(commit=False)
      #  user.email = self.cleaned_data["email"]
       # if commit:
        #    user.save()
        #return user

    
