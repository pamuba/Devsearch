from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, Skill

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'username', 'email', 'password1', 'password2']
        labels = {
            'first_name':'Name'
        }
    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        # self.fields['title'].widget.attrs.update({'class':'input'})
        for name, field in self.fields.items():
            field.widget.attrs.update({"class":"input"})
# Model + Form
class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'email', 'username', 'location', 'bio',
        'short_intro', 'profile_image', 'social_github', 'social_twitter',
        'social_linkedin','social_youtube','social_website']

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        # self.fields['title'].widget.attrs.update({'class':'input'})
        for name, field in self.fields.items():
            field.widget.attrs.update({"class":"input"})

class SkillForm(ModelForm):
    class Meta:
        model = Skill
        fields = '__all__'
        exclude = ['owner']

    def __init__(self, *args, **kwargs):
        super(SkillForm, self).__init__(*args, **kwargs)
        # self.fields['title'].widget.attrs.update({'class':'input'})
        for name, field in self.fields.items():
            field.widget.attrs.update({"class":"input"})
        