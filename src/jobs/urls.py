from django.urls import path
from django.contrib.auth.decorators import login_required

# from .views import IndexListView
from .views import (
					index_view, 
					jobpost_view, 
					JobPostCreateView, 
					JobsListView, 
					candidates_view, 
					contact_view, 
					JobsDetailView,
					JobPostUpdateView,
					JobPostDeleteView,
					PostedJobsListView,
					EmployerJobsListView,
					CategoryJobsListView,
					LocationJobsListView,
					JobsTypeListView,
					JobPostApplyView,
				)

app_name = 'jobs'

urlpatterns = [
    # path('', views.IndexView.as_view(), name='index'),
    path('', index_view, name='index'),
    path('jobs/employer/<str:username>/', EmployerJobsListView.as_view(), name='employer-jobs'),
    path('jobs/category/<str:category>/', CategoryJobsListView.as_view(), name='category-jobs'),
    path('jobs/location/<str:location>/', LocationJobsListView.as_view(), name='location-jobs'),
    path('jobs/type/<str:jobtype>/', JobsTypeListView.as_view(), name='type-jobs'),
    path('jobpost/', jobpost_view, name='jobpost'),
    path('jobpost/new/', login_required(JobPostCreateView.as_view()), name='jobpost-create'),
    path('jobs/<int:pk>/update/', login_required(JobPostUpdateView.as_view()), name='job-update'),
    path('jobs/<int:pk>/delete/', login_required(JobPostDeleteView.as_view()), name='job-delete'),
    path('jobs/', JobsListView.as_view(), name='jobslist'),
    path('posted-jobs/<str:username>/', PostedJobsListView.as_view(), name='posted-jobs'),
    path('jobs/<int:pk>/', JobsDetailView.as_view(), name='job-detail'),
    path('jobs/<int:pk>/apply/', login_required(JobPostApplyView.as_view()), name='job-apply'),
    path('candidates/', candidates_view, name='candidates'),
    path('contact/', contact_view, name='contact'),
]

