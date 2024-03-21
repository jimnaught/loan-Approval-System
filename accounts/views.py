from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            login(request, new_user)
            return redirect('predictions:home')

    else:
        form = UserRegistrationForm()

    context = {
        'form': form,
    }

    return render(request, 'registration/register.html', context)