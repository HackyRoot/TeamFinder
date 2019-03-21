from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from users.forms import UserRegisterForm
from django.shortcuts import render, redirect
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Profile
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from teams.models import Team
from django.views.generic import ListView, TemplateView, DetailView, UpdateView
from django.core.mail import EmailMessage, EmailMultiAlternatives
from django.template.loader import render_to_string
from django.template import Context


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            # username = form.cleaned_data.get('username')
            # messages.success(request, f'Account created for {username}!')
            # return redirect('home')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            username = form.cleaned_data.get('username')
            first_name = form.cleaned_data.get('first_name')
            messages.success(request, f'Hi  {first_name}, your account has been created!')
            return redirect('profile')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            user = p_form.save()
            user.refresh_from_db()
            user.bio = p_form.cleaned_data.get('bio')
            user.file = p_form.cleaned_data.get('file')
            user.team_name = p_form.cleaned_data.get('team_name')


            user.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form,
    }

    return render(request, 'users/profile.html', context)

# not so usefil
def profile_details(request, pk):
    # Current user id: request.user.pk
    # Viewing profile id: Profile.objects.filter(pk=pk)

    # user = User.objects.filter(pk=pk)
    profiles = Profile.objects.filter(user=pk) # current viewing profile object
    teams = Team.objects.filter(members=pk)
    team_data = Team.objects.all()
    lead_data = Team.objects.filter(team_lead=pk) # team list where current user is lead

    return render(request, 'users/profile_detail.html', context={'profiles': profiles,'lead_data': lead_data, 'teams': teams, 'team_data': team_data })
    # return HttpResponse(lead_data)

# class ProfileDetailsView(DetailView):
#     model = Profile

    # def get_context_data(self, **kwargs):
    #     context = super(ProfileDetailsView, self).get_context_data(**kwargs)
    #     # user_name = User.objects.get(username=self.request.user)
    #     context['lead_data'] = Team.objects.filter(team_lead=self.request.user.pk)
    #     context['myteams'] = Team.objects.filter(members=self.request.user.pk)
    #
    #     return context
    #
    # def test_func(self):
    #     profile = self.get_object()
    #     if self.request.user == profile.user:
    #         return True
    #     return False






# from django.views.generic import ListView, DetailView
# from django_filters import views
#


class ProfileListView(ListView):
    model = Profile
    context_object_name = 'profile_list'

    def get_context_data(self, **kwargs):
        context = super(ProfileListView, self).get_context_data(**kwargs)
        context['myteams'] = Team.objects.filter(team_lead_id=self.request.user)
        context['myteams'] = Team.objects.filter(members=self.request.user)

        return context


class MyTeamView(DetailView, UserPassesTestMixin, LoginRequiredMixin):
    model = Team

    context_object_name = 'myteam'

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Team.objects.filter(members=self.request.user)
        else:
            return Team.objects.none()

    def test_func(self):
        team = self.get_object()
        if self.request.user == team.team_lead:
            return True
        return False


def myteam(request, pk):
    lead_data = Team.objects.filter(team_lead=pk)
    teams = Team.objects.filter(members=pk)
    return render(request, 'users/my_teams.html', context={'teams': teams, 'lead_data': lead_data})

msg_plain = render_to_string('users/email.txt')
msg_html = render_to_string('users/email.html')


def sendInvite(request, pk):
    user_obj = Profile.objects.get(pk=pk)
    member_name = user_obj.user.username
    member_email = user_obj.user.email

    team = Team.objects.get(team_lead=request.user.id)
    team_name = team.team_name

    d = Context({'username': member_name})

    subject, from_email, to = 'hello', 'from@example.com', 'to@example.com'
    text_content = msg_plain.render(d)
    html_content = msg_html.render(d)
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(html_content, "text/html")
    msg.send()

    message = ' Hey there'
    email = EmailMessage(
        "Team Invitation",
        'Hello ',
        'from@example.com',
        ['to1@example.com', 'to2@example.com'],
        ['bcc@example.com'],
        reply_to=['another@example.com'],
        headers={'Message-ID': 'foo'},
    )
    email.send(fail_silently=True)
    return HttpResponse(member_name+' '+member_email+' '+team_name)