from django.urls import path
from . import views
from .views import TeamListView, TeamCreateView, \
    TeamDeleteView, TeamUpdateView, TeamDetailView, manage_team, InviteView, sendInvite


from django.urls import reverse
urlpatterns = [
    path('', TeamListView.as_view(), name='home'),
    path('team/new/', TeamCreateView.as_view(), name='team-create'),
    # path('team/<pk>/', team_detail, name='team-detail'),
    path('team/<pk>/', TeamDetailView.as_view(), name='team-detail'),
    # path('team/<pk>/', views.team_detail(pk=request.pk), name='team-detail'),
    path('team/<pk>/update/', TeamUpdateView.as_view()
         , name='team-update'),
    path('team/<pk>/delete/', TeamDeleteView.as_view(), name='team-delete'),
    path('about/', views.about, name='about'),
    path('profiles/<pk>/<operation>/', manage_team, name='manage_team'),
    path('invite/', InviteView.as_view(), name='invite_mem'),
    path('profiles/<pk>/<operation>/<team_name>/invitation/', views.sendInvite, name='send_invite'),
]
    # path('accounts/profile/add', views.add_member, name='add_member'),
    # path('accounts/profile/remove', views.remove_member, name='remove_member'),