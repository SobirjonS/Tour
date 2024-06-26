# Generated by Django 5.0.6 on 2024-06-25 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_feedbag_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='seats',
            field=models.SmallIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='booking',
            name='status',
            field=models.SmallIntegerField(choices=[(1, 'Bron qilingan'), (2, 'To`langan'), (3, 'Bekor qilingan')], default=1),
        ),
    ]
