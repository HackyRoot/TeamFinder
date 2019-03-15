from django.urls import path
from . import views
from .views import TeamListView, TeamDetailView, TeamCreateView

from django.urls import reverse
urlpatterns = [
    path('', TeamListView.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('team/new/', TeamCreateView.as_view(), name='team-create'),
    path('team/<pk>/', TeamDetailView.as_view(), name='team-detail'),

]