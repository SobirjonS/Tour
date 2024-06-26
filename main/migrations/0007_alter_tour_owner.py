# Generated by Django 5.0.6 on 2024-06-20 05:32

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_tour_owner_alter_customuser_avatar_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tour',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
