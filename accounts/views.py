from django.views.generic import TemplateView


class LoginApplicantView(TemplateView):
    template_name = 'login_applicant.html'


class LoginEmployerView(TemplateView):
    template_name = 'login_employer.html'


class RegisterView(TemplateView):
    template_name = 'register.html'
