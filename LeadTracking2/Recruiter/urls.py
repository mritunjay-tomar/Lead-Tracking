from django.urls import path
from . import views

app_name = "Recruiter"

urlpatterns = [
    path('', views.HandleLogin, name='login'),
    path('logout/', views.HandleLogout, name='logout'),
    path('home/', views.RecuriterHome, name='home'),
    path('register/', views.RegisterRecruiter, name='register-recruiter'),
    path('student/', views.AddStudent, name='new-student'),
    path('convert/', views.ConvertStudent, name='convert-student'),
    path('delete/', views.DeleteStudent, name='delete-student'),
    path('reinitial/', views.ReInitialStudent, name='reinitial'),
    path('page_not_found/', views.handler404, name="page_not_found"),
    path('server_error/', views.handler500, name="500_error")
]