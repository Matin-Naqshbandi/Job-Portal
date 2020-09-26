from django.contrib import admin
from .models import *
# Register your models here.

class JobPostAdmin(admin.ModelAdmin):
	fieldsets = [
        	('Jobpost information', {'fields': ['employer', 'title', 'category', 'jobtype', 'location', 'description', 'expire_date', 'experience', 'salary', 'post_date', 'permission']}),
	]
	list_display=('category', 'jobtype', 'title', 'employer', 'location', 'post_date', 'permission', 'was_posted_recently', 'is_available')
	list_filter=['post_date', 'permission', 'category', 'jobtype', 'location']
	search_fields = ['title']
	date_hierarchy = 'post_date'



admin.site.register(JobPost, JobPostAdmin)
admin.site.register(Category)
admin.site.register(JobStatus)
admin.site.register(JobApplication)
admin.site.register(JobType)
admin.site.register(Permission)