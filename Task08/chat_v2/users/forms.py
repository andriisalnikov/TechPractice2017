from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm, PasswordChangeForm
from users.models import Profile


class RegistrationForm(UserCreationForm):

    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    class Meta:

        model = User
        fields = (
            'username',
            'email',
            'password1',
            'password2'
        )

    def save(self, commit=True):

        user = super(RegistrationForm, self).save(commit=True)
        user.email = self.cleaned_data['email']

        if commit:
            user.save()
            
        return user

    def __init__(self, *args, **kwargs):

        # first call the 'real' __init__()
        super(RegistrationForm, self).__init__(*args, **kwargs)
        # then do extra stuff:
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['class'] = 'form-control'
        

class EditUserForm(UserChangeForm):

    class Meta:
        model = User
        fields = (
            'email',
            'username',
            'password'
        )
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),      
        }

class EditProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ('profile_photo',)

class LoginForm(AuthenticationForm):

    def __init__(self, *args, **kwargs):

        # first call the 'real' __init__()
        super(AuthenticationForm, self).__init__(None, *args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['class'] = 'form-control'
        # then do extra stuff:

class ChangePassswordForm(PasswordChangeForm):

    def __init__(self, *args, **kwargs):

        super(PasswordChangeForm, self).__init__(*args, **kwargs)
        
        self.fields['old_password'].widget.attrs['class'] = 'form-control'
        self.fields['new_password1'].widget.attrs['class'] = 'form-control'
        self.fields['new_password2'].widget.attrs['class'] = 'form-control'
