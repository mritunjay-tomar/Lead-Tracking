from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from django.utils.safestring import mark_safe

from Recruiter.models import Student as StudentModel
from Recruiter.FormUtils import utility
from Recruiter.LogicFiles import Student as StudentLogic

from django_countries.fields import CountryField
from django_countries.data import COUNTRIES
from django_countries.widgets import CountrySelectWidget


class UserRegistrationForm(forms.Form):

    FirstName = forms.CharField(
        max_length=30,
        label=mark_safe('First Name{}'.format(utility.GetRequiredSpan()))
    )
    LastName = forms.CharField(
        max_length=30,
        label=mark_safe('Last Name{}'.format(utility.GetRequiredSpan()))
    )
    Email = forms.EmailField(
        label=mark_safe('E-mail{}'.format(utility.GetRequiredSpan())),
        help_text=mark_safe("<small>Your E-mail will be your username</small>")
    )
    password1 = forms.CharField(
        label=mark_safe("Password{}".format(utility.GetRequiredSpan())),
        widget=forms.PasswordInput,
        help_text=mark_safe("<small>Password must be 8 characters long,<br> should contain both alphabets and numbers</small>")
    )
    password2 = forms.CharField(
        label=mark_safe("Confirm Password{}".format(utility.GetRequiredSpan())),
        widget=forms.PasswordInput,
        help_text=mark_safe("<small>Please enter same password again</small>")
    )

    class Meta:
        model = User
        fields = [
            'FirstName',
            'LastName',
            'Email',
            'password1',
            'password2'
        ]


    def saveUser(self):
        users = User.objects.all().filter(email=self.cleaned_data['Email'])
        if users.count() > 0:
            return "User email already exsits"
        if self.cleaned_data['password1'] != self.cleaned_data['password2']:
            return "Password's do not match"
        if len(self.cleaned_data['password1']) < 8:
            return "Password must be atleast 8 characters long"
        if not self.cleaned_data['password1'].isalnum():
            return "Password should contain both alphabets and numbers"

        user = User.objects.create_user(
            username=self.cleaned_data['Email'],
            email=self.cleaned_data['Email'],
            first_name=self.cleaned_data['FirstName'],
            last_name=self.cleaned_data['LastName']
        )
        user.set_password(self.cleaned_data['password1'])
        user.is_active = True
        user.is_staff = True
        user.is_superuser = False
        user.save()
        return ""


class StudentForm(forms.Form):
    FirstName = forms.CharField(
        max_length=30,
        label=mark_safe('First Name{}'.format(utility.GetRequiredSpan()))
    )
    MiddleName = forms.CharField(
        max_length=30,
        label='Middle Name',
        required=False
    )
    LastName = forms.CharField(
        max_length=30,
        label=mark_safe('Last Name{}'.format(utility.GetRequiredSpan()))
    )
    Email = forms.EmailField(
        label=mark_safe('E-mail{}'.format(utility.GetRequiredSpan()))
    )
    PhoneNumber = forms.CharField(
        max_length=12,
        label=mark_safe('Phone Number{}'.format(utility.GetRequiredSpan()))
    )
    AltNumber = forms.CharField(
        max_length=12,
        label='Alternate Phone Number',
        required=False
    )
    Country = CountryField(blank=True, multiple=True).formfield()
   # Country = forms.ChoiceField(choices=sorted(COUNTRIES.items()))

    class Meta:
        model = StudentModel

        fields = [
            'FirstName',
            'MiddleName',
            'LastName',
            'Email',
            'PhoneNumber',
            'AltNumber',
            'Country'
        ]
        

    def save(self, context):
        data = self.cleaned_data
        # If validation is required, please perform it before populating it on ORM class and return appropriate message
        student = StudentModel.objects.all().filter(Email=self.cleaned_data['Email'])
        if student.count() > 0:
            return "E-mail already exists"
        # Populate ORM values
        student = StudentModel()
        student.FirstName = data['FirstName']
        student.MiddleName = data['MiddleName']
        student.LastName = data['LastName']
        student.Email = data['Email']
        student.PhoneNumber = StudentLogic.GetPhoneNumberWithAltNumber(data['PhoneNumber'], data['AltNumber'])
        student.UserSavedBy = context['user_id']
        student.country = data['Country']
        student.save()

        return ""
