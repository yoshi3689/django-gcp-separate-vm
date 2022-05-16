from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .forms import AdvancedUserRegisterForm ,UserUpdateForm, ImageUpdateForm

def register(request):
  if request.method == 'POST':
    # grab onto the set of data that just got POSTed
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
        login(request, user)
        # it is important that I keep the below line as redirect instead of render
        # because render resubmits the data in the POST request
        return redirect('/profile')

  # if the use just came to this page, empty form will be rendered
  else:
    form = AdvancedUserRegisterForm()
  return render(request, 'users/register.html', {'form':form})

 
# adds a functionality to a existing function
@login_required
# take you to the profile page
def profile(request):
  if request.method == 'POST':
    # instantiates an form with the updated info if POST req was made
    u_form = UserUpdateForm(request.POST, instance=request.user)
    i_form = ImageUpdateForm(
      request.POST,
      request.FILES,
      instance=request.user.profile
      )
    if u_form.is_valid() and i_form.is_valid(): messages.success(request, f'Your account has been updated!')
    elif not i_form.is_valid(): messages.error(request, f'There was an error while updating your profile pic. Try it again!')
    elif not u_form.is_valid(): messages.success(request, f'There was an error while updating your profile info. Try it again!')
    if u_form.is_valid(): u_form.save()
    if i_form.is_valid(): i_form.save()

  else:
    # instantiate those forms with the logged in user's info
    u_form = UserUpdateForm(instance=request.user)
    i_form = ImageUpdateForm(instance=request.user.profile)

  context = {
      'u_form':u_form,
      'i_form':i_form,
      }
  
  return render(request, 'users/profile.html', context=context)