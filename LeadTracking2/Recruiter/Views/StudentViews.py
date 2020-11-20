from django.shortcuts import render, redirect

from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import user_passes_test
from django.contrib import messages

from Recruiter.models import Student as StudentORM
from Recruiter.forms import UserRegistrationForm, StudentForm
from Recruiter.LogicFiles import Student as StudentLogic
from Recruiter.Views import RecruiterViews


@user_passes_test(lambda u: u.is_superuser)
@login_required
def AddStudent(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            context = {
                'user_id': request.user.id
            }
            msg = form.save(context)
            if msg == "":
                messages.success(request, "Student added successfully")
                return RecruiterViews.RecuriterHome(request)
            else:
                messages.error(request, msg)
                return redirect("Recruiter:new-student")
        else:
            messages.error(request, "Error occurred while adding student")
    else:
        form = StudentForm()

    return render(request, "Recruiter/AddStudent.html", {"form": form})


@login_required
def ConvertStudent(request):
    studentID = int(request.GET.get('studentId'))
    user_first_name = str(request.GET.get('user_first_name'))
    user_last_name = str(request.GET.get('user_last_name'))
    StudentLogic.ConvertStudent(studentID, user_first_name+' '+user_last_name)
    messages.success(request, "Student converted successfully")
    return RecruiterViews.RecuriterHome(request)


@login_required
def ReInitialStudent(request):
    studentID = int(request.GET.get('studentId'))
    student_name = StudentLogic.ReInitializeStudent(studentID)
    messages.success(request, f"Student {student_name} re-initialized successfully")
    return RecruiterViews.RecuriterHome(request)


@login_required
def DeleteStudent(request):
    studentID = int(request.GET.get('studentId'))
    StudentLogic.DeleteStudent(studentID)
    messages.success(request, "Student deleted successfully")
    return RecruiterViews.RecuriterHome(request)


@login_required
def ArchiveStudent(request):
    return RecruiterViews.RecuriterHome(request)
