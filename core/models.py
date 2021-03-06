from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    last_profile_download_date = models.DateField(null=True, blank=True)


@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()


class Skills(models.Model):
    name = models.CharField(max_length = 30)

    def __str__(self):
        return self.name
 
    
class Course(models.Model):
    name = models.CharField(max_length = 30)
   
    def __str__(self):
        return self.name


class Location(models.Model):
    name = models.CharField(max_length = 50)
   
    def __str__(self):
        return self.name


class CandidateProfile(models.Model):
    serial_no = models.IntegerField(default=0)
    resume_status = models.BooleanField(default = False)
    name = models.CharField(max_length=100, blank=True)
    mobile = models.CharField(max_length=30, blank=True)
    email = models.CharField(max_length=30, blank=True)
    work_ex = models.FloatField(default=0.0)
    analytic_ex = models.FloatField(default=0.0)
    current_location = models.ForeignKey(Location , related_name = "current_location",null=True , blank=True)
    nearest_city = models.ForeignKey(Location , related_name = "nearest_city",null=True , blank=True)
    preferred_location = models.ForeignKey(Location , related_name = "preferred_location",null=True , blank=True)
    ctc = models.FloatField(default=0.0)
    current_employer = models.CharField(max_length=100, blank=True)
    current_designation = models.CharField(max_length=100, blank=True)
    skills = models.ManyToManyField(Skills,null=True , blank=True) 
    ug_course = models.ManyToManyField(Course,null=True , blank=True)
    year_of_passing = models.IntegerField(null=True , blank=True)
    
