from django.contrib.auth import authenticate, login, logout
from django.views.generic import TemplateView
from django.shortcuts import redirect

from .forms import LoginForm

class LoginApplicantView(TemplateView):
    template_name = 'login_applicant.html'
    form = LoginForm

    def get(self, request, *args, **kwargs):
        form = self.form()
        context = {'form': form}
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        form = self.form(request.POST)
        if not form.is_valid():
            return redirect('login_applicant')
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(request, username=username, password=password)
        if not user:
            return redirect('index')
        login(request, user)
        next = request.GET.get('next')
        if next:
            return redirect(next)
        return redirect('index')

def logout_view(request):
    logout(request)
    return redirect('index')


class LoginEmployerView(TemplateView):
    template_name = 'login_employer.html'


class RegisterView(TemplateView):
    template_name = 'register.html'
