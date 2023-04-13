from django.urls import path

from accounts.views import RegisterView, LoginEmployerView, LoginApplicantView, logout_view, ProfileView, \
    UserPasswordChangeView, UserChangeView

urlpatterns = [
    path('login/employer', LoginEmployerView.as_view(), name='login_employer'),
    path('login/applicant', LoginApplicantView.as_view(), name='login_applicant'),
    path('register/', RegisterView.as_view(), name='register'),
    path('logout/', logout_view, name='logout'),
    path('profile/<int:pk>', ProfileView.as_view(), name='detail'),
    path('profile/<int:pk>/change/', UserChangeView.as_view(), name='change'),
    path('<int:pk>/password_change', UserPasswordChangeView.as_view(), name='password_change'),
]
