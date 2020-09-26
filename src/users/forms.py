from django import forms
from django.contrib.auth.models import User as django_user
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, User, JobseekerProfile, EmployerProfile

class UserRegistrationForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'password1', 'password2', 'province', 'user_type']
		
class UserUpdateForm(forms.ModelForm):
	first_name = forms.CharField(required=False)
	last_name = forms.CharField(required=False)
	class Meta:
		model = User
		fields = ['username', 'first_name', 'last_name']


class ProfileUpdateForm(forms.ModelForm):
	picture = forms.ImageField(required=False)
	class Meta: 
		model = Profile
		fields = ['picture']

class EmployerUserUpdateForm(forms.ModelForm):
	class Meta:
		model=User
		fields = ['username']			

class EmployerUpdateForm(forms.ModelForm):
	organization = forms.CharField()
	website = forms.CharField(required=False)
	class Meta:
		model = EmployerProfile
		fields = ['organization', 'website']

class JobSeekerUpdateForm(forms.ModelForm):
	NotDiscuss = 'O'
	Male = 'M'
	Female = 'F'
	Genders_Choices = [ (NotDiscuss, 'Not Discuss'),(Male, 'Male'),(Female, 'Female')]

	gender = forms.ChoiceField(choices = Genders_Choices, required=False)
	dob = forms.DateField(widget=forms.TextInput(attrs={'type':'date','class':'datepicker'}), required=False)
	resume = forms.FileField(required=False)
	class Meta:
		model = JobseekerProfile
		fields = ['gender', 'dob', 'resume']



