from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group, Permission
from .models import CustomUser, UserProfile
from .models import AccessRule
from .models import IdentityInfo

class IdentityAccessForm(forms.ModelForm):
    class Meta:
        model = IdentityInfo
        fields = ['allowed_users']

class AccessRuleForm(forms.ModelForm):
    class Meta:
        model = AccessRule
        fields = ['target_user', 'can_access']
class SignUpForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('bio', 'birth_date')

class RoleForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ('name', 'permissions')

class AssignRoleForm(forms.Form):
    user = forms.ModelChoiceField(queryset=CustomUser.objects.all())
    role = forms.ModelChoiceField(queryset=Group.objects.all())


class UserPermissionsForm(forms.ModelForm):
    permissions = forms.ModelMultipleChoiceField(
        queryset=Permission.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = CustomUser
        fields = ['permissions']