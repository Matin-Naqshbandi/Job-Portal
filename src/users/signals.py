from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import User, Profile, UserType, EmployerProfile, JobseekerProfile


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
	if created: 
		if instance.user.user_type.id == 2:
			EmployerProfile.objects.create(user=instance)
		else:
			JobseekerProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
	instance.profile.save()



