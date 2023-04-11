# Generated by Django 4.2 on 2023-04-11 11:01

from django.db import migrations

def create_profiles(apps, schema_editor):
    User = apps.get_model('auth', 'User')
    ApplicantProfile = apps.get_model('accounts', 'ApplicantProfile')
    for user in User.objects.all():
        ApplicantProfile.objects.get_or_create(user=user)

class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_profiles, migrations.RunPython.noop)
    ]
