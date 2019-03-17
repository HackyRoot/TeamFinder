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
    created_on = models.DateField(default=timezone.now())
    members = models.ManyToManyField(User)



    def __str__(self):
        return f'{self.team_name}'

    def get_absolute_url(self):
        return reverse('team-detail', kwargs={'pk': self.pk})


    @classmethod
    def add_member(cls, current_team, member):
        mem_obj = cls.objects.get(
            team_name=current_team
        )
        mem_obj.members.add(member)

    @classmethod
    def remove_member(cls, current_team, member):
        mem_obj = cls.objects.get(
            team_name=current_team
        )
        mem_obj.members.remove(member)
    #
    # @classmethod
    # def remove_member(cls, current_team, member):
    #     mem_obj, created = cls.objects.get_or_create(
    #         current_team=current_team
    #     )
    #     mem_obj.members.remove(member)
    # @classmethod
    # def add_member(cls, current_team_lead, new_member):
    #     member, created = cls.objects.get_or_create(
    #         current_team_lead=current_team_lead
    #     )
    #     member.users.add(new_member)
    #
    # @classmethod
    # def remove_member(cls, a, new_member):
    #     member, created = cls.objects.get_or_create(
    #         current_team_lead=current_team_lead
    #     )
    #
    #     member.users.remove(new_member)


# https://simpleisbetterthancomplex.com/tutorial/2018/01/18/how-to-implement-multiple-user-types-with-django.html
# https://hashedin.com/blog/configure-role-based-access-control-in-django/

# https://stackoverflow.com/questions/29868086/implementing-a-model-for-teams-in-django
#



