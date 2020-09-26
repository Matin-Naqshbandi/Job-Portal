from django import forms
from .models import JobPost, JobApplication


class JobPostCreateForm(forms.ModelForm):
	class Meta:
		model = JobPost
		fields = ['title', 'category', 'jobtype', 'description', 'location', 'experience', 'salary']

class JobApplicationForm(forms.ModelForm):
	class Meta:
		model = JobApplication
		fields = ['job', 'jobseeker', 'status', 'apply_date']
