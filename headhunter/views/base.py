from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'index.html'

    # def get(self, request, *args, **kwargs):
    #     if not self.request.user.is_authenticated:
    #         return redirect('login_applicant')
    #     else:
    #         return super().get(request, *args, **kwargs)
