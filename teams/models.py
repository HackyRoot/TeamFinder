from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from users.models import User


class Team(models.Model):
    team_name = models.CharField(max_length=50, unique=True, default='', primary_key=True)
    description = models.TextField(max_length=1024, default='')
    team_image = models.ImageField(default='default.jpg', upload_to='team_pics')
    team_lead = models.ForeignKey(User, null=True, blank=True, default=None, on_delete=models.CASCADE)
    team_members = models.CharField(max_length=100, default='')

    # members = models.Oneto(User, blank=True, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.team_name}'

    def get_absolute_url(self):
        return reverse('team-detail', kwargs={'pk': self.pk})

# https://simpleisbetterthancomplex.com/tutorial/2018/01/18/how-to-implement-multiple-user-types-with-django.html
# https://hashedin.com/blog/configure-role-based-access-control-in-django/
# class TeamLead(models.Manager):
#     use_for_related_fields = True
#
#     def add_player(self, Team.team_name, Member.member_name):
#         g = Team.objects.get(name=Team.team_name)
#         g.user_set.add(member_name)
#
#     def remove_player(self, Team.team_name, member_name):
#         g = Group.objects.get(name=team)
#         g.user_set.add(member_name)
#
#     def trasnfer_player(self, team, member_name):
#         pass
# https://stackoverflow.com/questions/29868086/implementing-a-model-for-teams-in-django
#
# class Contact(models.Model):
#     team_c = models.ForeignKey(Team,  on_delete=models.CASCADE) # to_field=Team.team_name,
#     member_c = models.ForeignKey(Profile, on_delete=models.CASCADE) # to_field=User.username,

    # object = TeamLead


