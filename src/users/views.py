from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from users.models import Profile, Feedback
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from .forms import UserRegistrationForm, JobSeekerUpdateForm, ProfileUpdateForm, UserUpdateForm, EmployerUpdateForm, EmployerUserUpdateForm
# Create your views here.


# def login_view(request): # *args, **kwargs
#     return render(request, "users/login-page.html", {})


def register(request):
	if request.method == 'POST':
		form = UserRegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f'Hi {username}! \n Please login')
			return redirect('login')
	else:	
		form = UserRegistrationForm()
	return render(request, 'users/register.html', {'form':form})

def mailbox_view(request):
	return render(request, 'users/mailbox/mailbox.html')
def mailcompose_view(request):
	return render(request, 'users/mailbox/compose.html')
def mailread_view(request):
	return render(request, 'users/mailbox/read-mail.html')

def register_employer(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f'Hi {username}! \n Please login')
			return redirect('login')
	else:	
		form = UserCreationForm()
	return render(request, 'users/register_employer.html', {'form':form})


@login_required
def profile(request):
	if request.user.user.user_type.id == 3:
		if request.method == 'POST':
			u_form = UserUpdateForm(request.POST, instance=request.user)
			js_form = JobSeekerUpdateForm(request.POST,  request.FILES, instance=request.user.profile.jobseekerprofile)
			p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
			if u_form.is_valid and js_form.is_valid() and p_form.is_valid():
				u_form.save()
				js_form.save()
				p_form.save()
				messages.success(request, f'Your information has been updated!')
				return redirect('profile')

		else:
			u_form = UserUpdateForm(instance=request.user)
			js_form = JobSeekerUpdateForm(instance=request.user.profile.jobseekerprofile)
			p_form = ProfileUpdateForm(instance=request.user.profile)

		context = {
			'u_form' : u_form,
			'js_form' : js_form,
			'p_form' : p_form
		}
	else:
		if request.method == 'POST':
			u_form = EmployerUserUpdateForm(request.POST, instance=request.user)
			em_form = EmployerUpdateForm(request.POST,  request.FILES, instance=request.user.profile.employerprofile)
			p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
			if u_form.is_valid() and em_form.is_valid() and p_form.is_valid():
				u_form.save()
				em_form.save()
				p_form.save()
				messages.success(request, f'Your information has been updated!')
				return redirect('profile')

		else:
			u_form = EmployerUserUpdateForm(instance=request.user)
			em_form = EmployerUpdateForm(instance=request.user.profile.employerprofile)
			p_form = ProfileUpdateForm(instance=request.user.profile)

		context = {
			'u_form' : u_form,
			'em_form' : em_form,
			'p_form' : p_form
		}
	return render(request, 'users/profile.html', context)


# LoginRequiredMixin also makes sure that login is required
class FeedbackCreateView(LoginRequiredMixin, CreateView):
	model = Feedback
	fields = ['title', 'description']
	success_url = 'index.html'

	# specicfies the Feedback user
	def form_valid(self, form):
		form.instance.employer = self.request.user.user.profile.employerprofile
		return super().form_valid(form)