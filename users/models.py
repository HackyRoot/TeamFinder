from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import datetime
from django.urls import reverse
from PIL import Image
from multiselectfield import MultiSelectField
from teams.models import Team

SEX = [('male', 'Male'),
       ('female', 'Female'),
       ('other', 'Other')]

SKILLS = [('frontend', 'Front End'),
          ('backend', 'Back End'),
          ('fullstack_web', 'FullStack Web'),
          ('machine_learning', 'Machine Learning'),
          ('data_science', 'Data Science'),
          ('networking', 'Networking'),
          ('mobile_app_develop', 'Mobile App Development')]

CITIES = [('ahmedabad', 'Ahmedabad'),
          ('vadodara', 'Vadodara'),
          ('surat', 'Surat'),
          ('rajkot', 'Rajkot'),
          ('other', 'Other')]

QUAL = [('bachelors', 'Bachelors'),
        ('masters', 'Masters'),
        ('phd', 'PhD'),
        ('postdoc', 'PostDoc'),
        ('other', 'Other')]


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    bio = models.CharField(max_length=500, default='NA', blank=True)
    gender = models.CharField(max_length=6, choices=SEX, default='')
    skills = MultiSelectField(max_length=3000, choices=SKILLS, default='')
    city = models.CharField(max_length=20, choices=CITIES, default='')
    contact_no = models.CharField(blank=True, max_length=15, default='0')
    qualification = MultiSelectField(max_length=30, choices=QUAL, default='bachelors')
    team_name = models.ForeignKey(Team, to_field='team_name', on_delete=models.CASCADE,
                                  related_name='team_profile', blank=True, null=True)

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, **kwargs):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

    def get_absolute_url(self):
        return reverse('profile_data', kwargs={'pk': self.pk })


