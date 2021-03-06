from .views import register, profile, ProfileListView, myteam, profile_details, sendInvite
from django.urls import path
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('register/', register, name='register'),
    path('profiles/list/', ProfileListView.as_view(), name='profile-list'),
    path('profiles/<pk>/', profile_details, name='profile_data'),
    path('accounts/profile/', profile, name='profile'),
    path('profiles/<pk>/team/', myteam, name='myteam'),
    path('profiles/<pk>/invite/', sendInvite, name='sendInvite'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    # path('test/', test_mail, 'test')

]
