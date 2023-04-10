from django.urls import path

from accounts.views import RegisterView, LoginEmployerView, LoginApplicantView

urlpatterns = [
    path('login/employer', LoginEmployerView.as_view(), name='login_employer'),
    path('login/applicant', LoginApplicantView.as_view(), name='login_applicant'),
    path('register/', RegisterView.as_view(), name='register')
]
