# Generated by Django 3.2.10 on 2021-12-21 22:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kineticapi', '0004_auto_20211215_2047'),
    ]

    operations = [
        migrations.AddField(
            model_name='athleteevent',
            name='completed',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='activitysport',
            name='activity',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='activity_sports', to='kineticapi.activity'),
        ),
    ]
