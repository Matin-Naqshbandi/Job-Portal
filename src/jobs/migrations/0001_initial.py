# Generated by Django 2.2.6 on 2019-11-19 19:48

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=50)),
                ('description', models.CharField(blank=True, max_length=500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='JobStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='JobType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jobtype', models.CharField(max_length=50)),
                ('description', models.CharField(blank=True, max_length=500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='JobPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, max_length=1000, null=True)),
                ('experience', models.IntegerField(blank=True, null=True)),
                ('salary', models.IntegerField(blank=True, null=True)),
                ('post_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date Posted')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='jobs.Category')),
                ('employer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Employer')),
                ('jobtype', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='jobs.JobType')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='users.Province')),
                ('permission', models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='users.Permission')),
            ],
        ),
        migrations.CreateModel(
            name='JobApplication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apply_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date Applied')),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobs.JobPost')),
                ('jobseeker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Jobseeker')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='jobs.JobStatus')),
            ],
            options={
                'unique_together': {('job', 'jobseeker')},
            },
        ),
    ]