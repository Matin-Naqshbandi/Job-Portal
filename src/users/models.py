import datetime
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User as django_user
from PIL import Image
from .validators import validate_file_extension, validate_image_extension

# Create your models here.

class UserType(models.Model):
    user_type = models.CharField(max_length=50)
    def __str__(self):
        return self.user_type

class Province(models.Model):
    province = models.CharField(max_length=50)
    def __str__(self):
        return self.province


# class User(models.Model):
#     create_date = models.DateTimeField('User create date', default=timezone.now)

#     def was_created_recently(self):
#         return self.create_date >= timezone.now() - datetime.timedelta(days=7)
#     was_created_recently.admin_order_field = 'create_date'
#     was_created_recently.boolean = True
#     was_created_recently.short_description = 'Created recently?'

#     def __str__(self):
#         return self.username
class User(django_user):
    user_type = models.ForeignKey(UserType, on_delete=models.PROTECT)
    province = models.ForeignKey(Province, on_delete=models.PROTECT)

        

class Profile(models.Model):
    user = models.OneToOneField(django_user, on_delete=models.CASCADE)
    picture = models.ImageField(default='default.png',upload_to='pictures/%Y/%m/%d/', validators=[validate_image_extension], blank=True)
    # def was_created_recently(self):
    #         return self.create_date >= timezone.now() - datetime.timedelta(days=7)
    # was_created_recently.admin_order_field = 'create_date'
    # was_created_recently.boolean = True
    # was_created_recently.short_description = 'Created recently?'

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)
        img = Image.open(self.picture.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.picture.path)
        

class SecurityQuestion(models.Model):
    question = models.CharField(max_length=255)
    def __str__(self):
        return self.question

class SecurityAnswer(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    question = models.ForeignKey(SecurityQuestion, on_delete=models.CASCADE)
    answer = models.CharField(max_length= 50)

    # class Meta: 
    #     unique_together = ('user', 'question')

    def __str__(self):
        return self.answer

class Message(models.Model):
    m_from = models.ForeignKey(django_user, related_name='message', on_delete=models.CASCADE)
    m_to = models.ForeignKey(django_user, related_name='mto', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=1000)
    sent_date = models.DateTimeField('Sent Date', default=timezone.now)
    reply = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.title

class JobseekerProfile(Profile):
    Male = 'M'
    Female = 'F'
    NotDiscuss = 'O'
    Genders_Choices = [(Male, 'Male'),(Female, 'Female'), (NotDiscuss, 'Not Discuss')]

    gender = models.CharField(max_length=1, choices = Genders_Choices, default=NotDiscuss)
    dob = models.DateField('Date of Birth', blank=True, null=True)
    resume = models.FileField(upload_to='resumes/%Y/%m/%d/', validators=[validate_file_extension], blank=True)

    def __str__(self):
        return self.user.username

class EmployerProfile(Profile):
    organization = models.CharField(max_length=50, blank=True, null=True)
    website = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.user.username

class Feedback(models.Model):
    user = models.ForeignKey(django_user, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    sent_date = models.DateTimeField('Sent Date', default=timezone.now)

    def __str__(self):
        return self.title