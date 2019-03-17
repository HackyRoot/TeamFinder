from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Team
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from users.models import Profile
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import TeamManageForm
from django.core.mail import send_mail
from django.http import HttpResponse

def home(request):
    # context = {
    #     'team_list': Team.objects.all()
    # }
    context = {
        'team_list': Team.objects.all()
    }
    return render(request, 'teams/home.html', context)

def sendInvite(request, pk, operation, team_name):
    invitee = User.objects.get(username=pk)
    invitee_email = invitee.email
    res = send_mail("hello paul", "comment tu vas?", "paul@polo.com", [invitee_email], [operation], [team_name])
    return HttpResponse('%s' % res)
    # http://127.0.0.1:8000/profiles/2/add/A%20Team/invitation/


class InviteView(TemplateView):
    template_name = 'teams/team_manage.html'

    def post(self, request):
        form = TeamManageForm()
        team_names = Team.objects.filter(team_lead=request.user)
        members = Profile.objects.exclude(user=request.user)

        args = {'form': form, 'team_names': team_names, 'members': members}
        return render(request, self.template_name, args)




class TeamListView(ListView):
    model = Team
    template_name = 'teams/home.html'
    context_object_name = 'team_list'
    ordering = ['team_name']

    # page_kwarg = ['[k']


class TeamDetailView(DetailView):
    model = Team





# def team_detail(request, pk):
#
#     context = {
#         'team_data': Team.objects.all(),
#         # 'member': Team.objects.filter(team_name_id=request.team_name),
#     }
#     return render(request, 'teams/team_detail.html', context)


class TeamCreateView(LoginRequiredMixin, CreateView):
    model = Team
    fields = ['team_name', 'description', 'team_image']

    # success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.team_lead = self.request.user
        return super().form_valid(form)


class TeamUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Team
    fields = ['description', 'team_image']


    def form_valid(self, form):
        form.instance.team_lead = self.request.user
        return super().form_valid(form)

    def test_func(self):
        team = self.get_object()
        if self.request.user == team.team_lead:
            return True
        return False


class TeamDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Team
    success_url = '/'

    def test_func(self):
        team = self.get_object()
        if self.request.user == team.team_lead:
            return True
        return False

# def change_member(request, operation, usernmae):


class HomeView(TemplateView):
    template_name = 'teams/home.html'

    def get(self, request, *args, **kwargs):
        form = HomeView()
        teams = Team.objects.all().order_by('team_name')
        users = User.objects.exclude(id=request.user.id)


def about(request):
    user = User.objects.get(username=request.user)
    return HttpResponse(user.id)
    # return render(request, 'teams/about.html')


def team(request):
    context = {
        'team_list': Team.objects.all()
    }
    return render(request, 'teams/team.html', context)


def manage_team(request, operation, pk):
    # userid = member_profile_id
    # request.user = team_lead_name
    # team = Team.objects.get(team_lead=2)
    # team_name = team.team_name
    #
    # if request.method == 'POST':
    #     form = TeamManageForm(request.user, request.POST)
    #     if form.is_valid():
    #         mem = form.save()
    #         mem.user = request.user
    #         mem.save()
    #         return redirect('team-detail')
    # else:
    #     form = TeamManageForm(request.user)
    # return render(request, 'teams/team.html', {'form':form})

    # try:
    #     user_obj = User.objects.get(pk=pk)
    #     team = Team.objects.get(team_lead=request.user.id)
    #
    #     member_name = user_obj.user.username
    #     team_name = team.team_name
    #
    # except User.DoesNotExist or Team.DoesNotExist:
    #     return None

    user_obj = Profile.objects.get(pk=pk)
    member_name = user_obj.user.username

    team = Team.objects.get(team_lead=request.user.id)
    team_name = team.team_name

    if operation == 'add':
        Team.add_member(team_name, pk)
        messages.success(request, f'Added {member_name} in {team_name}!')


    elif operation == 'remove':
        Team.remove_member(team_name, pk)
        messages.warning(request, f'Removed {member_name} from {team_name}!')
    else:
        return redirect('home')
    return redirect('home')


    # context = {
    #     'user': User.objects.all(),
    #     'team': Team.objects.all(),
    #     'profile': Profile.objects.all()
    # }
    # return render(request, 'teams/team_manage.html', context)
    # return redirect('home')
#

