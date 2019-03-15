from django.urls import path
from . import views
from .views import TeamListView, TeamDetailView, TeamCreateView, TeamDeleteView, TeamUpdateView


from django.urls import reverse
urlpatterns = [
    path('', TeamListView.as_view(), name='home'),
    path('team/new/', TeamCreateView.as_view(), name='team-create'),
    path('team/<pk>/', TeamDetailView.as_view(), name='team-detail'),
    path('team/<pk>/update/', TeamUpdateView.as_view(), name='team-update'),
    path('team/<pk>/delete/', TeamDeleteView.as_view(), name='team-delete'),
    path('about/', views.about, name='about'),
    # path('accounts/profile/add', views.add_member, name='add_member'),
    # path('accounts/profile/remove', views.remove_member, name='remove_member'),
]