# Generated by Django 3.2.9 on 2021-12-05 00:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kineticapi', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='sport',
        ),
        migrations.AddField(
            model_name='event',
            name='event_sport',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='event_sports', to='kineticapi.eventsport'),
            preserve_default=False,
        ),
    ]