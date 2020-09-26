from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import JobPost, Category, JobType, JobApplication
from users.models import EmployerProfile, JobseekerProfile, Province
from django.contrib.auth.models import User
from .forms import JobPostCreateForm, JobApplicationForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
	ListView, 
	DetailView,
	CreateView,
	UpdateView,
	DeleteView
	)
# Create your views here.

def index_view(request):
	context = {
		'JobPost': JobPost.objects.all().order_by('-post_date'),
		'Category': Category.objects.all(),
		'EmployerProfile': EmployerProfile.objects.all(),
		'JobseekerProfile': JobseekerProfile.objects.all(),
		'Province': Province.objects.all(),
		'JobType': JobType.objects.all(),
		}
	return render(request, "index.html", context)


class JobsListView(ListView):
	model = JobPost
	template_name = 'jobs/jobs-list.html' # default: <app>/<model>_<viewtype>.html
	context_object_name = 'JobPost'
	ordering = ['-post_date']
	paginate_by = 5

class EmployerJobsListView(ListView):
	model = JobPost
	template_name = 'jobs/employer-jobs.html' # default: <app>/<model>_<viewtype>.html
	context_object_name = 'JobPost'
	paginate_by = 5

	# get username from url
	# and query jobposts form it
	def get_queryset(self):
		user = get_object_or_404(User, username=self.kwargs.get('username'))
		return JobPost.objects.filter(employer=user.profile.employerprofile).order_by('-post_date')

class CategoryJobsListView(ListView):
	model = JobPost
	template_name = 'jobs/category-jobs.html' # default: <app>/<model>_<viewtype>.html
	context_object_name = 'JobPost'
	paginate_by = 5

	# get username from url
	# and query jobposts form it
	def get_queryset(self):
		category = get_object_or_404(Category, category=self.kwargs.get('category'))
		return JobPost.objects.filter(category=category).order_by('-post_date')

class LocationJobsListView(ListView):
	model = JobPost
	template_name = 'jobs/location-jobs.html' # default: <app>/<model>_<viewtype>.html
	context_object_name = 'JobPost'
	paginate_by = 5

	# get username from url
	# and query jobposts form it
	def get_queryset(self):
		province = get_object_or_404(Province, province=self.kwargs.get('location'))
		return JobPost.objects.filter(location=province).order_by('-post_date')

class JobsTypeListView(ListView):
	model = JobPost
	template_name = 'jobs/job-type.html' # default: <app>/<model>_<viewtype>.html
	context_object_name = 'JobPost'
	paginate_by = 5

	# get username from url
	# and query jobposts form it
	def get_queryset(self):
		jobtype = get_object_or_404(JobType, jobtype=self.kwargs.get('jobtype'))
		return JobPost.objects.filter(jobtype=jobtype).order_by('-post_date')

class PostedJobsListView(ListView):
	model = JobPost
	template_name = 'jobs/posted-jobs.html' # default: <app>/<model>_<viewtype>.html
	context_object_name = 'JobPost'
	paginate_by = 5

	# get username from url
	# and query jobposts form it
	def get_queryset(self):
		user = get_object_or_404(User, username=self.kwargs.get('username'))
		return JobPost.objects.filter(employer=user.profile.employerprofile).order_by('-post_date')


class JobsDetailView(DetailView):
	model = JobPost
	template_name = 'jobs/job-detail.html'
	

def candidates_view(request):
	return render(request, "jobs/candidates.html", {})

def contact_view(request):
	return render(request, "contact.html", {})

# LoginRequiredMixin also makes sure that login is required
class JobPostCreateView(LoginRequiredMixin, CreateView):
	model = JobPost
	fields = ['title', 'category', 'jobtype', 'location', 'description', 'expire_date', 'experience', 'salary']

	# if you want to get redirected to home page after submit
	# success_url = 'index.html'
	# specicfies the jobpost employer
	def form_valid(self, form):
		form.instance.employer = self.request.user.user.profile.employerprofile
		return super().form_valid(form)

# LoginRequiredMixin also makes sure that login is required
class JobPostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = JobPost
	fields = ['title', 'category', 'jobtype', 'location', 'description', 'experience', 'salary']

	# if you want to get redirected to home page after submit
	# success_url = 'index.html'
	# specicfies the jobpost employer
	def form_valid(self, form):
		form.instance.employer = self.request.user.user.profile.employerprofile
		return super().form_valid(form)

	# making sure the person who wants to update jobpost is the same person who posted it
	def test_func(self):
		jobpost = self.get_object()
		if self.request.user == jobpost.employer.employerprofile.user:
			return True
		return False


class JobPostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = JobPost
	success_url = "/posted-jobs"

	# making sure the person who wants to update jobpost is the same person who posted it
	def test_func(self):
		jobpost = self.get_object()
		if self.request.user == jobpost.employer.employerprofile.user:
			return True
		return False

class JobPostApplyView(LoginRequiredMixin, CreateView):
	model = JobApplication
	fields = ['job', 'jobseeker', 'status', 'apply_date']
	template_name = 'jobs/job-apply.html'
	# if you want to get redirected to home page after submit
	success_url = 'index.html'
	# specicfies the jobpost employer
	# def form_valid(self, form):
	# 	form.instance.employer = self.request.user.user.profile.employerprofile
	# 	return super().form_valid(form)

# @login_required
# def jobapplication_view(request, **kwargs):
# 	jobapply = get_object_or_404(JobPost, id=kwargs.get('pk'))

# 	return render(request, 'jobs/job-apply.html',{})


# # LoginRequiredMixin also makes sure that login is required
# class JobApplicationView(LoginRequiredMixin, CreateView):
# 	model = JobApplication
# 	fields = ['job', 'jobseeker', 'status', 'apply_date']
# 	template_name = 'jobs/job-apply.html'

# 	# if you want to get redirected to home page after submit
# 	# success_url = 'index.html'
# 	# specicfies the jobpost employer
# 	def form_valid(self, form):
# 		form.instance.jobseeker = self.request.user.user.profile.jobseekerprofile
# 		return super().form_valid(form)


def jobpost_view(request):
	return render(request, "jobs/job-post.html", {})

# class IndexListView(ListView):

# 	def get_context_data(self, **kwargs):
#          context = super(IndexListView, self).get_context_data(**kwargs)
#          context['JobPost'] = JobPost.objects.all()
#          context['Category'] = Category.objects.all()
#          context['EmployerProfile'] = EmployerProfile.objects.all()
#          context['JobseekerProfile'] = JobseekerProfile.objects.all()
#          context['Province'] = Province.objects.all()
#          context['JobType'] = JobType.objects.all()
#          return context

# 	template_name = 'index.html' # <app>/<model>_<viewtype>.html
# 	context_object_name = get_context_data()

# @login_required
# def newpost_view(request):
# 	if request.method == 'POST':
# 		jpcform= JobPostCreateForm(request.POST, instance= request.user.user.profile.employerprofile)
# 		if jpcform.is_valid():
# 			jpcform.objects.create(employer=request.user.user.profile.employerprofile)
# 			jpcform.save()
# 			messages.success(request,f'posted successfuly!')
# 			return redirect('jobs:index')
# 	else:
# 		jpcform = JobPostCreateForm(instance= request.user.user.profile.employerprofile)
# 	return render(request, "jobs/new-post.html", {'jpcform' : jpcform})
