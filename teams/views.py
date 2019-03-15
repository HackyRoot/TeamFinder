from django.shortcuts import render
from .models import Team
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from users.models import Profile
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
def home(request):
    # context = {
    #     'team_list': Team.objects.all()
    # }
    context = {
        'team_list': Team.objects.all()
    }
    return render(request, 'teams/home.html', context)


class TeamListView(ListView):
    model = Team
    template_name = 'teams/home.html'
    context_object_name = 'team_list'
    ordering = ['team_name']


class TeamDetailView(DetailView):
    model = Team


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
    return render(request, 'teams/about.html')


def team(request):
    context = {
        'team_list': Team.objects.all()
    }
    return render(request, 'teams/team.html', context)

