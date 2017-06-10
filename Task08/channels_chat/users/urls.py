from django.conf.urls import url
from users.views import RegisterView, home, view_profile, EditProfileView, ChangePasswordView, change_friends, LoginView, change_friend_request, delete_current_account, user_management, delete_account, block_account
from django.contrib.auth.views import login, logout, password_reset, password_reset_done, password_reset_confirm, password_reset_complete

urlpatterns = [
    url(r'^$', home, name="home"),
    url(r'^login/$', LoginView.as_view(), name="login"),
    url(r'^login$', LoginView.as_view(), name="login"),
    url(r'^logout/$', logout, {'next_page': 'chat:home'}, name="logout"),
    url(r'^register/$', RegisterView.as_view(), name="register"),
    url(r'^view/$', view_profile, name="view_profile"),
    url(r'^edit/$', EditProfileView.as_view(), name="edit_profile"),
    url(r'^change-password/$', ChangePasswordView.as_view(), name="change_password"),
    url(r'^connect/(?P<action>.+)/(?P<pk>\d+)$', change_friends, name="change_friends"),
    url(r'^change_friend_request/(?P<action>.+)/(?P<pk>\d+)$', change_friend_request, name="change_friend_request"),
    url(r'^delete/$', delete_current_account, name="delete_current_account"),
    url(r'^user-management/$', user_management, name="user_management"),
    url(r'^delete_account/(?P<userID>\d+)$', delete_account, name="delete_account"),
    url(r'^block_account/(?P<userID>\d+)$', block_account, name="block_account"),
    url(r'^reset-password/$', password_reset, {'template_name': 'users/reset_password.html', 'post_reset_redirect': 'users:password_reset_done', 'email_template_name':'users/reset_password_email.html', 'from_email': 'infochatroom13@gmail.com'}, name='reset_password'),
    url(r'^reset-password/done/$', password_reset_done, {'template_name':'users/reset_password_done.html'}, name='password_reset_done'),
    url(r'^reset-password/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', password_reset_confirm, {'template_name': 'users/reset_password_confirm.html', 'post_reset_redirect': 'users:password_reset_complete'}, name='password_reset_confirm'),
    url(r'^reset-password/complete/$', password_reset_complete, {'template_name': 'users/reset_password_complete.html'}, name='password_reset_complete'),
]