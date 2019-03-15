from django.shortcuts import render
from .models import Team
from django.views.generic import ListView, DetailView, CreateView
from users.models import Profile
from django.urls import reverse, reverse_lazy

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


class TeamCreateView(CreateView):
    model = Team
    fields = ['team_name', 'description', 'team_image']

    # success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.team_lead = self.request.user
        return super().form_valid(form)


def about(request):
    return render(request, 'teams/about.html')


def team(request):
    context = {
        'team_list': Team.objects.all()
    }
    return render(request, 'teams/team.html', context)

