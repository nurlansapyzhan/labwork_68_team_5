from django.urls import path

from headhunter.views import IndexView, Resume, ResumeDetail, ResumeCreateView, ResumeUpdateView, ResumeDeleteView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('resume/add/', ResumeCreateView.as_view(), name='resume_add'),
    path('resume/add/', ResumeCreateView.as_view(), name='resume_add'),
    path('resumes/<int:pk>/', ResumeDetail.as_view(), name='resume_view'),
    path('resume/<int:pk>/update/', ResumeUpdateView.as_view(), name='resume_update'),
    path('resume/<int:pk>/delete/', ResumeDeleteView.as_view(), name='resume_delete'),
    path('resume/<int:pk>/confirm_delete/', ResumeDeleteView.as_view(), name='resume_delete'),
]