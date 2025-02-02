# Generated by Django 3.2.21 on 2024-05-27 11:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('iam_app', '0002_accessrule'),
    ]

    operations = [
        migrations.CreateModel(
            name='IdentityInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('bio', models.TextField(blank=True)),
                ('allowed_users', models.ManyToManyField(blank=True, related_name='allowed_identity_infos', to=settings.AUTH_USER_MODEL)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
