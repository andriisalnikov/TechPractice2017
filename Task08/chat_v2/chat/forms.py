from django import forms
from chat.models import Chat_room, Chat_group
from django.forms import ModelForm
from users.models import User, Friend
from django.db.models import Q


class RoomEditForm(ModelForm):

    class Meta:

        model = Chat_room
        fields = (
            'title',
            'background_color',
        )
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'background_color': forms.TextInput(attrs={'class': 'form-control jscolor'}),      
        }

class GroupRoomEditForm(ModelForm):
    
    class Meta:

        model = Chat_group
        fields = (
            'title',
            'background_color',
            'users',
            'chat_admin'
        )
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'background_color': forms.TextInput(attrs={'class': 'form-control jscolor'}),
            'users': forms.CheckboxSelectMultiple(attrs={'class': 'form-control'}),
            'chat_admin': forms.HiddenInput()
        }
    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user")
        
        super(GroupRoomEditForm, self).__init__(*args, **kwargs)

        friends = {}
        try:
            friend = Friend.objects.get(current_user=user)
            friends = friend.users.all()
        except:
            pass
        friend_ids = []

        for item in friends:
            friend_ids.append(item.pk)

        self.fields['users'].queryset = User.objects.filter(pk__in = friend_ids)

class EmailForm(forms.Form):
    subject = forms.CharField()
    email = forms.EmailField()
    message = forms.CharField()
    