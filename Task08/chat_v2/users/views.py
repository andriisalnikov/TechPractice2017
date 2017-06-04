# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse, render_to_response
from django.views.generic import TemplateView
from users.forms import RegistrationForm, EditProfileForm, EditUserForm, LoginForm, ChangePassswordForm
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash, login, authenticate
from django.contrib.auth.models import User
from models import Friend, Friend_request
from chat.models import Chat_room
from django.db.models import Q
from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
import datetime
from django.utils import timezone
from django.contrib.auth.decorators import login_required





# Create your views here.


class RegisterView(TemplateView):

    def get(self, request):
        form = RegistrationForm()
        args = {'form': form}
        return render(request, 'users/register.html', args)

    def post(self, request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            new_user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password1'],
                                    )
            login(request, new_user)
            return redirect('/')
        else:
            return render(request, 'users/register.html', {'form': form})


class EditProfileView(TemplateView):
    
    def get(self, request):
        user_form = EditUserForm(instance=request.user)
        profile_form = EditProfileForm(instance=request.user.profile)
        args = {'user_form': user_form, 'profile_form': profile_form}
        return render(request, 'users/edit_profile.html', args)

    def post(self, request):
        user_form = EditUserForm(request.POST, instance=request.user)
        profile_form = EditProfileForm(request.POST, request.FILES, instance=request.user.profile)
        
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('users:view_profile')
        return HttpResponse("Something went wrong")

class ChangePasswordView(TemplateView):
    def get(self, request):
        form = ChangePassswordForm(user=request.user)
        args = {'form': form}
        return render(request, 'users/change-password.html', args)
    def post(self, request):
        form = PasswordChangeForm(data=request.POST, user=request.user);
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('users:view_profile')
        else:
            return redirect('users:change_password')

def view_profile(request):
    user = request.user
    args = {'user': user}
    return render(request, 'users/profile.html', args)

@login_required
def home(request):
    return render(request, 'users/home.html', {})

def change_friends(request, action, pk):
    if not request.user.is_authenticated():
        return redirect('chat:home')
    elif int(pk) == int(request.user.pk):
        return redirect('chat:home')
    else:
        new_user = User.objects.get(pk=pk)
        if action == 'add':
            
            if Chat_room.objects.filter((Q(user1=request.user) & Q(user2=new_user)) | (Q(user2=request.user) & Q(user1=new_user)) ).exists():
                pass
            else:
                room = Chat_room(user1=request.user, user2=new_user)
                room.save()
            
            Friend.make_friend(request.user, new_user)
            Friend.make_friend(new_user, request.user)

            requestUserObj = Friend_request.objects.get(current_user=request.user)
            userRequestedFriendshipObj = Friend_request.objects.get(current_user=User.objects.get(pk=pk))
            
            requestUserObj.requests_received.remove(User.objects.get(pk=pk))
            userRequestedFriendshipObj.requests_sent.remove(request.user)
            
        elif action == 'loose':
            Friend.lose_friend(request.user, new_user)
            Friend.lose_friend(new_user, request.user)
        return redirect('chat:home')

def change_friend_request(request, action, pk):

    try:
        currentUserObj = Friend_request.objects.get(current_user=request.user)
    except:
        currentUserObj = Friend_request.objects.create(current_user=request.user)

    try:
        friendObj = Friend_request.objects.get(current_user=User.objects.get(pk=pk))
    except:
        friendObj = Friend_request.objects.create(current_user=User.objects.get(pk=pk))

    if action=="send":
        currentUserObj.requests_sent.add(User.objects.get(pk=pk))
        friendObj.requests_received.add(request.user)
    elif action=="cancel":
        currentUserObj.requests_sent.remove(User.objects.get(pk=pk))
        friendObj.requests_received.remove(request.user)

    return redirect('chat:home')


class LoginView(TemplateView):

    def get(self, request):
        form = LoginForm()
        args = {'form': form}
        return render(request, 'users/login.html', args)

    def post(self, request):
        form = AuthenticationForm(request, data=request.POST)
        form.fields['username'].widget.attrs['class'] = 'form-control'
        form.fields['password'].widget.attrs['class'] = 'form-control'
        if form.is_valid():

            user = User.objects.get(pk=form.get_user_id())
            if user.profile.block_expire > timezone.now():
                messages.warning(request, 'Your account is blocked until ' + str(user.profile.block_expire))
                return redirect('/')
            else:
                login(request, form.get_user())
                return redirect('/')
        else:
            return render(request, 'users/login.html', {'form': form})

def delete_current_account(request):
    currentUser = User.objects.get(pk=request.user.pk)
    currentUser.delete()
    messages.success(request, 'Your account has been deleted!')
    return redirect('users:login')

@staff_member_required
def user_management(request):
    users = User.objects.filter(is_staff=False)
    args = {'users': users, 'now': timezone.now()}
    return render(request, 'users/user_management.html', args)

@staff_member_required
def delete_account(request, userID):
    targetuser = User.objects.get(pk=userID)
    targetuser.delete()
    messages.success(request, 'The account has been deleted!')
    return redirect('users:user_management')

@staff_member_required
def block_account(request, userID):
    targetuser = User.objects.get(pk=userID)
    date = datetime.datetime.now()
    date += datetime.timedelta(minutes=1)
    targetuser.profile.block_expire = date
    targetuser.save()
    messages.success(request, 'The account has been blocked!')
    return redirect('users:user_management')
