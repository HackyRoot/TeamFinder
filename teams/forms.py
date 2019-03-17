from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# from .models import Member, Team


# https://stackoverflow.com/questions/49198400/django-add-user-to-team
# class InviteMemberForm(forms.ModelForm):
#
#     class Meta:
#         model = Team
#         fields = ['team_members', 'team_name']
#
#     def __init__(self,user,*args,**kwargs):
#         super(InviteMemberForm,self ).__init__(*args,**kwargs)
#         self.fields['team_name'].queryset = Team.objects.filter(id__in = Team.objects.filter('team' = user))


from django import forms
from teams.models import Team
from users.models import Profile

Team.objects.filter()

class TeamManageForm(forms.Form):
    team_name = forms.ChoiceField()
    member_email = forms.EmailField()

    class Meta:
        model = Team
        fields = ('team_name', 'team_lead', 'team_image', )

    def __init__(self, user, *args, **kwargs):
        super(TeamManageForm, self).__init__(*args, **kwargs)
        self.fields['members'].queryset = Profile.objects.filter(user=user)

