# Generated by Django 5.0.6 on 2024-06-24 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_rename_tourvideo_tourmedia_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedbag',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
