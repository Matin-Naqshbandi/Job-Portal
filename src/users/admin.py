from django.contrib import admin
from .models import *
# Register your models here.


# class UserSecurityAnswerInline(admin.TabularInline):
# 	model = SecurityAnswer
# 	extra = 2


# class UserAdmin(admin.ModelAdmin):
# 	fieldsets = [
#         	('User information', {'fields': ['username', 'password', 'picture', 'create_date', 'user_type', 'province', 'permission']}),
# 	]
# 	inlines = [UserSecurityAnswerInline]
# 	list_display = ('username', 'user_type', 'province', 'create_date', 'permission', 'was_created_recently')
# 	list_filter=['user_type', 'permission', 'create_date']
# 	search_fields = ['username']
# 	date_hierarchy = 'create_date'


# class UserSecurityAnswerAdmin(admin.ModelAdmin):
# 	list_display = ('user', 'answer')

# class UserMessageAdmin(admin.ModelAdmin):
# 	list_display = ('m_from', 'm_to', 'title', 'sent_date', 'reply')
# 	list_filter=['sent_date']
# 	search_fields = ['title']
# 	date_hierarchy = 'sent_date'



# # class JobseekerAdmin(admin.ModelAdmin):
# # 	fieldsets = [
# #         	('Employer information', {'fields': ['firstname', 'lastname', 'username', 'password', 'gender','dob', 'picture', 'resume', 'create_date', 'user_type', 'province', 'permission']}),
# # 	]
# # 	inlines = [UserSecurityAnswerInline]
# # 	list_display = ('username', 'firstname', 'lastname', 'gender', 'province', 'dob', 'permission', 'was_created_recently')
# # 	list_filter=['create_date', 'permission', 'gender','dob' , 'province']
# # 	search_fields = ['username']
# # 	date_hierarchy = 'create_date'



# class EmployerAdmin(admin.ModelAdmin):
# 	fieldsets = [
#         	('Employer information', {'fields': ['username', 'password', 'date_joined', 'is_active', 'organization', 'website']}),
# 	]
# 	# inlines = [UserSecurityAnswerInline]
# 	list_display = ('username', 'organization', 'date_joined')
# 	# list_filter=['create_date', 'permission', 'province']
# 	search_fields = ['username']
# 	date_hierarchy = 'date_joined'



# # admin.site.register(User, UserAdmin)
admin.site.register(UserType)
admin.site.register(Province)
# admin.site.register(Permission)
# admin.site.register(SecurityQuestion)
# admin.site.register(SecurityAnswer, UserSecurityAnswerAdmin)
# admin.site.register(Message, UserMessageAdmin)
admin.site.register(JobseekerProfile)
admin.site.register(EmployerProfile)
admin.site.register(Profile)
admin.site.register(User)
admin.site.register(Feedback)