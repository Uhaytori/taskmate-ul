from django.shortcuts import render, redirect
from .forms import CustomRegisterForm, LoginForm
from django.contrib import messages
from django.contrib.auth import login, authenticate  # add to imports

def register(request):
    if request.method=="POST":
        register_form = CustomRegisterForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request, ("new user account created, login to continue"))
            return redirect('register')
    register_form = CustomRegisterForm()
    return render(request, 'register.html', {'register_form':register_form})


def login_page(request):
    form = forms.LoginForm()
    message = ''
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                message = f'Hello {user.username}! You have been logged in'
            else:
                message = 'Login failed!'
        return redirect('todolist')
    return render(
        request, 'login.html', context={'form': form, 'message': message})


# def logout_page(request):
#     """logout logged in user"""
#     logout(request)
#     return HttpResponseRedirect(reverse_lazy('custom_auth:dashboard'))
