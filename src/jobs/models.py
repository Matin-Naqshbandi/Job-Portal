import datetime
from django.utils import timezone
from django.db import models
from users.models import Province, EmployerProfile, JobseekerProfile
from django.urls import reverse
# Create your models here.

class Category(models.Model):
	category = models.CharField(max_length=50)
	description = models.CharField(max_length=500, blank = True, null = True)
	def __str__(self):
		return self.category

class JobType(models.Model):
	jobtype = models.CharField(max_length=50)
	description = models.CharField(max_length=500, blank = True, null = True)
	def __str__(self):
		return self.jobtype
		
class Permission(models.Model):
    title = models.CharField(max_length = 50)
    description = models.CharField(max_length = 255)
    def __str__(self):
        return self.title

class JobPost(models.Model):
	employer = models.ForeignKey(EmployerProfile, on_delete=models.CASCADE)
	title = models.CharField(max_length=100)
	category = models.ForeignKey(Category, on_delete=models.PROTECT)
	jobtype = models.ForeignKey(JobType, on_delete=models.PROTECT)
	description = models.TextField(max_length=1000, blank = True, null = True)
	location = models.ForeignKey(Province, on_delete=models.PROTECT)
	experience = models.IntegerField(blank = True, null = True)
	salary = models.IntegerField(blank = True, null = True)
	post_date = models.DateTimeField('Date Posted', default=timezone.now)
	expire_date = models.DateField('Job Expiration Date', default=timezone.now() + datetime.timedelta(days=7))
	permission = models.ForeignKey(Permission, on_delete=models.PROTECT, default=1)
	def was_posted_recently(self):
		return self.post_date >= timezone.now() - datetime.timedelta(days=7)
	was_posted_recently.admin_order_field = 'post_date'
	was_posted_recently.boolean = True
	was_posted_recently.short_description = 'Posted recently?'

	#jobpost expire checker
	def is_available(self):
		return self.expire_date >= datetime.date.today()
	is_available.admin_order_field = 'post_date'
	is_available.boolean = True
	is_available.short_description = 'Is available?'

	def __str__(self):
		return self.title
	# get primary key for jobpost detail view
	def get_absolute_url(self):
		return reverse('jobs:job-detail', kwargs={'pk':self.pk})


class JobStatus(models.Model):
	status = models.CharField(max_length=50)
	def __str__(self):
		return self.status

class JobApplication(models.Model):
	job = models.ForeignKey(JobPost, on_delete=models.CASCADE)
	jobseeker = models.ForeignKey(JobseekerProfile, on_delete=models.CASCADE)
	status = models.ForeignKey(JobStatus, on_delete=models.PROTECT, default=1)
	apply_date = models.DateTimeField('Date Applied', default=timezone.now)
	class Meta: 
		unique_together = ('job', 'jobseeker')