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

from teams.models import Team
from django.views.generic import ListView, TemplateView, DetailView, UpdateView
# from .filters import UserFilter
# https://stackoverflow.com/questions/36327377/searching-with-modelchoicefield-in-django

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
            messages.success(request, f'Hi  {username}!, your account has been created! You are now able to login!')
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


class ProfileDetailsView(DetailView):
    model = Profile

    # def get(self, request, *args, **kwargs):
    #     return self.request.user.username

    # def get_object(self):

    #
    # def get_context_data(self, **kwargs):
    #     context = super(ProfileDetailsView, self).get_context_data(**kwargs)
    #     context['team_lead'] = Team.objects.filter(team_lead_id=self.request.user) # add extra field to the context
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


#
# class UserDetailView(DetailView):
#     model = User
#     template_name = views

#
#

