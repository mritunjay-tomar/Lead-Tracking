from django.shortcuts import render, redirect

from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib import messages


def HandleLogin(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data.get('username'), password=form.cleaned_data.get('password'))
            if user is not None:
                login(request, user)
                request.session['fName'] = user.first_name
                request.session['lName'] = user.last_name
                messages.add_message(request, messages.SUCCESS, f"Logged in as {form.cleaned_data.get('username')}")
                return redirect('Recruiter:home')
            else:
                messages.add_message(request, messages.ERROR, "Invalid username or password")
        else:
            messages.add_message(request, messages.ERROR, "Invalid username or password")
    else:
        form = AuthenticationForm()

    return render(request, 'Recruiter/login.html', {"form": form})


@login_required
def HandleLogout(request):
    logout(request)
    return redirect('Recruiter:login')


def handler404(request, exception):
    return render(request, "DefaultTemplates/404.html")

def handler500(request, exception):
    return render(request, "DefaultTemplates/505.html")