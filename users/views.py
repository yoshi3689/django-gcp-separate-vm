from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .forms import AdvancedUserRegisterForm 
# ,UserUpdateForm, ImageUpdateForm

def register(request):
  if request.method == 'POST':
    form = AdvancedUserRegisterForm(request.POST)
    if form.is_valid():
      # without the save function, nothing gets saved!!
      form.save()
      # form is valid when it is submitted
      username = form.cleaned_data.get('username')
      password = form.cleaned_data.get('password1')
      user = authenticate(request, username=username, password=password)
      if user:
        # template literal in python
        messages.success(request, f'Welcome {username}!')
        # it is important that I keep the below line as redirect instead of render
        # because render resubmits the data in the POST request
        return redirect('/profile')
  else:
    form = AdvancedUserRegisterForm()
  return render(request, 'users/register.html', {'form':form})


# adds a functionality to a existing function
# @login_required
# def profile(request):
#   if request.method == 'POST':
#   # what does the first argument do?
#     u_form = UserUpdateForm(request.POST, instance=request.user)
#     i_form = ImageUpdateForm(request.POST,
#     request.FILES,
#     instance=request.user.profile)
#     if u_form.is_valid() and i_form.is_valid():
#       u_form.save()
#       i_form.save()
#   else:
#     u_form = UserUpdateForm(instance=request.user)
#     i_form = ImageUpdateForm(instance=request.user.profile)

#   context = {
#       'u_form':u_form,
#       'i_form':i_form,
#       }
  
#   return render(request, 'users/profile.html', context)