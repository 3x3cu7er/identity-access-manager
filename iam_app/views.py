from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required, permission_required
from .forms import SignUpForm, UserProfileForm, RoleForm, AssignRoleForm, UserPermissionsForm
from .models import CustomUser
from django.contrib.auth.models import Group

def signup(request):
    if request.method == 'POST':
        user_form = SignUpForm(request.POST)
        profile_form = UserProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            raw_password = user_form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('profile')
    else:
        user_form = SignUpForm()
        profile_form = UserProfileForm()
    return render(request, 'signup.html', {'user_form': user_form, 'profile_form': profile_form})

def profile(request):
    user_profile = request.user.userprofile
    return render(request, 'profile.html', {'user_profile': user_profile})

def create_role(request):
    if request.method == 'POST':
        form = RoleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('roles')
    else:
        form = RoleForm()
    return render(request, 'create_role.html', {'form': form})

def assign_role(request):
    if request.method == 'POST':
        form = AssignRoleForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data['user']
            role = form.cleaned_data['role']
            user.roles.add(role)
            return redirect('roles')
    else:
        form = AssignRoleForm()
    return render(request, 'assign_role.html', {'form': form})

def roles(request):
    roles = Group.objects.all()
    return render(request, 'roles.html', {'roles': roles})


@login_required
def list_users(request):
    users = CustomUser.objects.filter(id=request.user.id)
    return render(request, 'list_users.html', {'users': users})

@login_required
def manage_user_permissions(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)
    
    # Check if the user being managed is the current user
    if request.user != user:
        return redirect('list_users')  # Redirect to list_users if trying to manage permissions for another user
    
    if request.method == 'POST':
        form = UserPermissionsForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('list_users')
    else:
        form = UserPermissionsForm(instance=user)
    return render(request, 'manage_user_permissions.html', {'form': form, 'user': user})
from django.shortcuts import render, redirect, get_object_or_404
from .models import AccessRule,IdentityInfo
from .forms import AccessRuleForm,IdentityAccessForm

def access_rules(request):
    rules = AccessRule.objects.filter(user=request.user)
    return render(request, 'access_rules.html', {'rules': rules})

def add_access_rule(request):
    if request.method == 'POST':
        form = AccessRuleForm(request.POST)
        if form.is_valid():
            rule = form.save(commit=False)
            rule.user = request.user
            rule.save()
            return redirect('access_rules')
    else:
        form = AccessRuleForm()
    return render(request, 'add_access_rule.html', {'form': form})

def edit_access_rule(request, rule_id):
    rule = get_object_or_404(AccessRule, id=rule_id, user=request.user)
    if request.method == 'POST':
        form = AccessRuleForm(request.POST, instance=rule)
        if form.is_valid():
            form.save()
            return redirect('access_rules')
    else:
        form = AccessRuleForm(instance=rule)
    return render(request, 'edit_access_rule.html', {'form': form})


@login_required
def manage_identity_access(request):
    identity_info = IdentityInfo.objects.get_or_create(user=request.user)[0]
    if request.method == 'POST':
        form = IdentityAccessForm(request.POST, instance=identity_info)
        if form.is_valid():
            form.save()
            return redirect('view_identity_info')
    else:
        form = IdentityAccessForm(instance=identity_info)
    return render(request, 'manage_identity_access.html', {'form': form})
