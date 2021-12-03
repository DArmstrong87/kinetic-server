# Generated by Django 3.2.9 on 2021-12-03 22:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kineticapi', '0004_alter_eventsport_event'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='sports',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='event_sports', to='kineticapi.eventsport'),
        ),
    ]
