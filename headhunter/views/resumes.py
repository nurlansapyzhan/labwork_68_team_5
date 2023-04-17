from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView

from headhunter.forms import ResumeForm
from headhunter.models import Resume


class ResumeDetail(DetailView):
    template_name = 'resume.html'
    model = Resume


class GroupPermissionMixin(UserPassesTestMixin):

    def test_func(self):
        return self.request.user.groups.filter(name__in=['admin', 'developer']).exists()


class ResumeCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    template_name = 'resume_create.html'
    form_class = ResumeForm
    success_url = '/'

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            form.user = request.user
            form.save()
            return redirect(self.success_url)
        context = {'form': form}
        return self.render_to_response(context)


class ResumeUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    template_name = 'resume_update.html'
    form_class = ResumeForm
    model = Resume
    groups = ['admin', 'manager']

    def get_success_url(self):
        return reverse('resume_view', kwargs={'pk': self.object.pk})


class ResumeDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    template_name = 'resume_confirm_remove.html'
    model = Resume
    success_url = reverse_lazy('index')
