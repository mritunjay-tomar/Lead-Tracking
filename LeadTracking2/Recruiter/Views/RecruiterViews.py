from django.shortcuts import render, redirect

from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import user_passes_test
from django.contrib import messages

from Recruiter.models import Student as StudentORM
from Recruiter.forms import UserRegistrationForm, StudentForm
from Recruiter.LogicFiles import Student as StudentLogic
from Recruiter.Views import views


@user_passes_test(lambda u: u.is_superuser)
@login_required
def RegisterRecruiter(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            msg = form.saveUser()
            if msg == "":
                messages.success(request, "Account Created Successfully")
                return RecuriterHome(request)
            else:
                messages.error(request, msg)
                return redirect("Recruiter:register-recruiter")
    else:
        form = UserRegistrationForm()

    return render(request, "Recruiter/register.html", {"form": form})


@login_required
def RecuriterHome(request):
    context = {
        "Student": StudentORM.objects.raw(StudentLogic.GetStudentSQL())
    }
    return render(request, 'Recruiter/home.html', context)

