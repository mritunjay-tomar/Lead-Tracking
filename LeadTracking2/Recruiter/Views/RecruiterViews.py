from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import User
from django.contrib import messages

from Recruiter.models import Student as StudentORM
from Recruiter.forms import UserRegistrationForm
from Recruiter.LogicFiles import Student as StudentLogic
from Recruiter.LogicFiles import Recruiter as RecruiterLogic


@login_required
@user_passes_test(lambda u: u.is_superuser)
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


@login_required
@user_passes_test(lambda u: u.is_superuser)
def ShowArchiveStudents(request):
    context = {
        "ShowArchiveStudents": True,
        "Student": StudentORM.objects.raw(StudentLogic.GetArchiveStudentSQL())
    }
    return render(request, 'Recruiter/home.html', context)


@login_required
@user_passes_test(lambda u: u.is_superuser)
def ShowAllRecruiters(request):
    context = {
        "Recruiters": User.objects.raw(RecruiterLogic.GetRecruiterList())
    }
    return render(request, 'Recruiter/ShowAllRecruiters.html', context)
