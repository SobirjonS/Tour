# Generated by Django 5.0.6 on 2024-06-21 06:32

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_category_alter_book_options_alter_customuser_options_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='TourVideo',
            new_name='TourMedia',
        ),
        migrations.RenameField(
            model_name='tour',
            old_name='description',
            new_name='body',
        ),
        migrations.RenameField(
            model_name='tour',
            old_name='name',
            new_name='place_name',
        ),
        migrations.RenameField(
            model_name='tourservice',
            old_name='service_description',
            new_name='service',
        ),
        migrations.RemoveField(
            model_name='tour',
            name='owner',
        ),
        migrations.AddField(
            model_name='tour',
            name='creator',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tour',
            name='discount',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='tour',
            name='title',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('for_connect', models.CharField(max_length=255)),
                ('token', models.TextField()),
                ('status', models.SmallIntegerField(choices=[(1, 'Bron qilingan'), (2, 'To`langan'), (3, 'Bekor qilingan')])),
                ('buyer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('tour', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.tour')),
            ],
            options={
                'verbose_name': 'Bron',
                'verbose_name_plural': 'Bronlar',
            },
        ),
        migrations.DeleteModel(
            name='Book',
        ),
    ]