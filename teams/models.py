from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from users.models import User
from django.utils import timezone


class Team(models.Model):
    team_name = models.CharField(max_length=50, unique=True, default='', primary_key=True)
    team_lead = models.ForeignKey(User, null=True, blank=True, default=None, on_delete=models.CASCADE, related_name='team_lead_key')
    description = models.TextField(max_length=1024, default='')
    team_image = models.ImageField(default='default.jpg', upload_to='team_pics')
    # team_members = models.ManyToManyField(User, through='Contact')
    created_on = models.DateField(default=timezone.now())

    # members = models.Oneto(User, blank=True, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.team_name}'

    def get_absolute_url(self):
        return reverse('team-detail', kwargs={'pk': self.pk})


class TeamManagement(models.Model):
    users = models.ManyToManyField(User)
    current_team_lead = models.ForeignKey(User, related_name="lead", null=True, on_delete=models.CASCADE)
    is_invited = models.BooleanField(default=False, null=False)

    @classmethod
    def add_member(cls, current_team_lead, new_member):
        member, created = cls.objects.get_or_create(
            current_team_lead=current_team_lead
        )
        member.users.add(new_member)

    @classmethod
    def remove_member(cls, current_team_lead, new_member):
        member, created = cls.objects.get_or_create(
            current_team_lead=current_team_lead
        )
        member.users.remove(new_member)

# https://www.youtube.com/watch?v=nwpLCa79DUw
#     def remove_player(self, user_c, team_c):
#         g = Team.objects.get(name=user_c)
#         g.user_set.remove(user_c)

    # def trasnfer_player(self, user_c, team_c):
    #     pass


# class Contact(models.Model):
#     team_c = models.ForeignKey(Team,  on_delete=models.CASCADE) # to_field=Team.team_name,
#     user_c = models.ForeignKey(User, on_delete=models.CASCADE) # to_field=User.username,
#
#     object = TeamLead


# https://simpleisbetterthancomplex.com/tutorial/2018/01/18/how-to-implement-multiple-user-types-with-django.html
# https://hashedin.com/blog/configure-role-based-access-control-in-django/

# https://stackoverflow.com/questions/29868086/implementing-a-model-for-teams-in-django
#



