from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('profile/', views.profile, name='profile'),
    path('create_role/', views.create_role, name='create_role'),
    path('assign_role/', views.assign_role, name='assign_role'),
    path('roles/', views.roles, name='roles'),
    path('users/', views.list_users, name='list_users'),
    path('users/<int:user_id>/permissions/', views.manage_user_permissions, name='manage_user_permissions'),
    path('access_rules/', views.access_rules, name='access_rules'),
    path('add_access_rule/', views.add_access_rule, name='add_access_rule'),
    path('edit_access_rule/<int:rule_id>/', views.edit_access_rule, name='edit_access_rule'),
    path('identity/access/', views.manage_identity_access, name='manage_identity_access'),
]
