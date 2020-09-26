# from django.db.models.signals import pre_save
# from django.dispatch import receiver
# from .models import JobPost


# @receiver(pre_save, sender=JobPost)
# def post_job(sender, instance, created, **kwargs):
# 	if created: 
# 		JobPost.objects.create(employer=instance)
# 		print(request)


# @receiver(pre_save, sender=JobPost)
# def post_job(sender, instance, **kwargs):
# 	instance.jobpost.save()



