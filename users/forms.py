from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile
from teams.models import Team
from django.core.validators import RegexValidator
from django_select2.forms import Select2MultipleWidget

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


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    # this sets the order of the fields
    class Meta:
        model = User
        fields = ("first_name", "last_name", "email", "username", "password1", "password2")


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    contact_no = forms.IntegerField(required=True, validators = [RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                    message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")])

    # team_name = forms.ModelMultipleChoiceField(required=False, queryset=Team.objects.all(), widget=Select2MultipleWidget)
    file = forms.FileField(required=False, widget=forms.ClearableFileInput)

    class Meta:
        model = Profile
        fields = ['image', 'contact_no', 'qualification', 'bio', 'gender', 'skills', 'city']

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Team.objects.filter(title__icontains=query)
        else:
            return Team.objects.all()

