from django.contrib import admin

from headhunter.models import Resume


# Register your models here.

class ResumeAdmin(admin.ModelAdmin):
    fields = ('category', 'name', 'salary', )

admin.site.register(Resume, ResumeAdmin)
