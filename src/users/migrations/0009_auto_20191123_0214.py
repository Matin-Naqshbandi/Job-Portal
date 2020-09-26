# Generated by Django 2.2.6 on 2019-11-22 21:44

from django.db import migrations, models
import users.validators


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_auto_20191122_2351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employerprofile',
            name='organization',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='employerprofile',
            name='website',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='jobseekerprofile',
            name='resume',
            field=models.FileField(blank=True, upload_to='resumes/%Y/%m/%d/', validators=[users.validators.validate_file_extension]),
        ),
        migrations.AlterField(
            model_name='profile',
            name='picture',
            field=models.ImageField(blank=True, default='default.png', upload_to='pictures/%Y/%m/%d/', validators=[users.validators.validate_image_extension]),
        ),
    ]
