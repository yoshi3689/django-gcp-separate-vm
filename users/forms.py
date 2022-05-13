from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from users.models import Profile
# from accounts.models import CustomUser
# from phone_field import PhoneField

# inherit from UserCreationForm
class AdvancedUserRegisterForm(UserCreationForm):
  # by default(without having to pass anything) it's a required field
  email = forms.EmailField()

  class Meta():
    model = User
    fields = UserCreationForm.Meta.fields + ('first_name', 'last_name', 'email')

  def clean_email(self):
    email = self.cleaned_data.get('email')
    if User.objects.filter(email=email).exists():
        raise forms.ValidationError("A user with that email already exists.")

  # has to have these two fields in the user table 
  # to see if it's actually working or not
  # def clean_name(self):
  #   first_name = self.cleaned_data.get('first_name')
  #   last_name = self.cleaned_data.get('last_name')
  #   if User.objects.filter(first_name=first_name).exists() and User.objects.filter(last_name=last_name).exists():
  #       raise forms.ValidationError("A user with that name already exists.")

  # user name check already is in place
  # def check_username(self):
  #   username = self.cleaned_data.get('username')
  #   if User.objects.filter(username=username).exists():
  #       raise forms.ValidationError("Username is not unique")


  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.fields['username'].widget.attrs['placeholder'] = 'Username'
    self.fields['email'].widget.attrs['placeholder'] = 'Email'
    self.fields['password1'].widget.attrs['placeholder'] = 'Password'
    self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        
    # fields = ['username', 'email', 'password1', 'password2']
  
# class UserUpdateForm(forms.ModelForm):
#   class Meta:
#     model = User
#     fields = ['username', 'email']
#   def clean_email(self):
#     email = self.cleaned_data.get('email')
#     if User.objects.filter(email=email).exists():
#         raise forms.ValidationError("That email is already used by another user.")

# class ImageUpdateForm(forms.ModelForm):
#   class Meta:
#     model = Profile
#     fields = ['image', 'age']
