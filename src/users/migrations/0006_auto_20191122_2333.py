# Generated by Django 2.2.6 on 2019-11-22 19:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
        ('users', '0005_auto_20191122_2323'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Employer',
            new_name='EmployerProfile',
        ),
        migrations.RenameModel(
            old_name='Jobseeker',
            new_name='JobseekerProfile',
        ),
    ]