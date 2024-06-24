# Generated by Django 5.0.6 on 2024-06-20 10:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_tour_seats_delete_tourseat'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Kategoriya',
                'verbose_name_plural': 'Kategoriyalar',
            },
        ),
        migrations.AlterModelOptions(
            name='book',
            options={'verbose_name': 'Bron', 'verbose_name_plural': 'Bronlar'},
        ),
        migrations.AlterModelOptions(
            name='customuser',
            options={'verbose_name': 'Foydalanuvchi', 'verbose_name_plural': 'Foydalanuvchilar'},
        ),
        migrations.AlterModelOptions(
            name='feedbag',
            options={'verbose_name': 'Izox', 'verbose_name_plural': 'Izohlar'},
        ),
        migrations.AlterModelOptions(
            name='raiting',
            options={'verbose_name': 'Baho', 'verbose_name_plural': 'Baholar'},
        ),
        migrations.AlterModelOptions(
            name='tour',
            options={'verbose_name': 'Sayohat', 'verbose_name_plural': 'Sayohatlar'},
        ),
        migrations.AlterModelOptions(
            name='tourimage',
            options={'verbose_name': 'Rasm', 'verbose_name_plural': 'Rasmlar'},
        ),
        migrations.AlterModelOptions(
            name='tourservice',
            options={'verbose_name': 'Xizmat', 'verbose_name_plural': 'Xizmatlar'},
        ),
        migrations.AlterModelOptions(
            name='tourvideo',
            options={'verbose_name': 'Video', 'verbose_name_plural': 'Vodeolar'},
        ),
        migrations.AddField(
            model_name='tour',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.category'),
        ),
    ]