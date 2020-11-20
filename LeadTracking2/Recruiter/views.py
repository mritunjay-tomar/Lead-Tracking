from django.shortcuts import render, redirect

from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import user_passes_test
from django.contrib import messages

from Recruiter.models import Student as StudentORM
from Recruiter.forms import UserRegistrationForm, StudentForm

from Recruiter.LogicFiles import Student as StudentLogic


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
                return RecuriterHome(request)
            else:
                messages.error(request, msg)
                return redirect("Recruiter:new-student")
        else:
            messages.error(request, "Error occurred while adding student")
    else:
        form = StudentForm()

    return render(request, "Recruiter/AddStudent.html", {"form": form})


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


@login_required
def RecuriterHome(request):
    context = {
        "Student": StudentORM.objects.raw(StudentLogic.GetStudentSQL())
    }
    return render(request, 'Recruiter/home.html', context)


@login_required
def ConvertStudent(request):
    studentID = int(request.GET.get('studentId'))
    user_first_name = str(request.GET.get('user_first_name'))
    user_last_name = str(request.GET.get('user_last_name'))
    StudentLogic.ConvertStudent(studentID, user_first_name+' '+user_last_name)
    messages.success(request, "Student converted successfully")
    return RecuriterHome(request)

@login_required
def ReInitialStudent(request):
    studentID = int(request.GET.get('studentId'))
    student_name = StudentLogic.ReInitializeStudent(studentID)
    messages.success(request, f"Student {student_name} re-initialized successfully")
    return RecuriterHome(request)

@login_required
def DeleteStudent(request):
    studentID = int(request.GET.get('studentId'))
    StudentLogic.DeleteStudent(studentID)
    messages.success(request, "Student deleted successfully")
    return RecuriterHome(request)


def handler404(request, exception):
    return render(request, "DefaultTemplates/404.html")

def handler500(request, exception):
    return render(request, "DefaultTemplates/505.html")