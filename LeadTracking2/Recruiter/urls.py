from django.urls import path
from Recruiter.Views import views, StudentViews, RecruiterViews

app_name = "Recruiter"

urlpatterns = [
    path('', views.HandleLogin, name='login'),
    path('logout/', views.HandleLogout, name='logout'),
    path('home/', RecruiterViews.RecuriterHome, name='home'),
    path('register/', RecruiterViews.RegisterRecruiter, name='register-recruiter'),
    path('student/', StudentViews.AddStudent, name='new-student'),
    path('convert/', StudentViews.ConvertStudent, name='convert-student'),
    path('delete/', StudentViews.DeleteStudent, name='delete-student'),
    path('archive/', StudentViews.ArchiveStudent, name='mark-student-archive'),
    path('archivestudent/', RecruiterViews.ShowArchiveStudents, name='archive-student'),
    path('showrecruiters/', RecruiterViews.ShowAllRecruiters, name='show-recruiters'),
    path('reinitial/', StudentViews.ReInitialStudent, name='reinitial'),
    path('page_not_found/', views.handler404, name="page_not_found"),
    path('server_error/', views.handler500, name="500_error")
]