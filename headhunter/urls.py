from django.urls import path

from headhunter.views import IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='index')
]