# Generated by Django 3.1 on 2020-09-09 00:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0003_auto_20200908_2328'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='following',
        ),
        migrations.AddField(
            model_name='user',
            name='following',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='followers', to=settings.AUTH_USER_MODEL),
        ),
    ]
