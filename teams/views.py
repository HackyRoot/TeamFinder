from django.shortcuts import render
from .models import Team

team_list = [
    {
        'team_id': 'SVIT001',
        'created_on': 'May 1, 2018',
        'team_lead': 'Pratik Parmar',
        'team_members': ['Deep Chaudhari','Vishal Rathva', 'Sahil Rathva']

    },
    {
        'team_id': 'SVIT002',
        'created_on': 'May 2, 2018',
        'team_lead': 'Yash Parekh',
        'team_members': ['Hardik Macchi', 'Akash Tarpada', 'Rishi Shah']
    }
]

def home(request):
    # context = {
    #     'team_list': Team.objects.all()
    # }
    context = {
        'team_list': team_list
    }
    return render(request, 'teams/home.html')


def about(request):
    return render(request, 'teams/about.html')


def team(request):
    context = {
        'team_list': Team.objects.all()
    }
    return render(request, 'teams/team.html', context)
