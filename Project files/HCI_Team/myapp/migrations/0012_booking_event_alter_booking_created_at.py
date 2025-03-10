# Generated by Django 4.1.5 on 2023-06-25 07:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_remove_booking_event_booking_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='event',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='myapp.events_list'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
