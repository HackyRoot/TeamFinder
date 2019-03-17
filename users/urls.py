from .views import register, ProfileDetailsView, profile, ProfileListView
from django.urls import path
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('register/', register, name='register'),
    path('profiles/list/', ProfileListView.as_view(), name='profile-list'),
    path('profiles/<pk>/', ProfileDetailsView.as_view(), name='profile_data'),
    path('accounts/profile/', profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),

]


