from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .models import ApplicantProfile


class ProfileInline(admin.StackedInline):
    model = ApplicantProfile
    fields = ('phone', 'birth_date', 'location',
              'sex', 'citizenship', 'has_experience',
              'experience_year', 'has_driving_lis',
              'bio', 'avatar')


class ProfileAdmin(UserAdmin):
    inlines = (ProfileInline, )


User = get_user_model()
admin.site.unregister(User)
admin.site.register(User, ProfileAdmin)