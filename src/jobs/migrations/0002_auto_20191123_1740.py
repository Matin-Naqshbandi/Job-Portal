# Generated by Django 2.2.6 on 2019-11-23 13:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Permission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=255)),
            ],
        ),
        migrations.AlterField(
            model_name='jobpost',
            name='permission',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='jobs.Permission'),
        ),
    ]