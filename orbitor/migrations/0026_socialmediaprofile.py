# Generated by Django 4.2.3 on 2023-09-28 06:16

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orbitor', '0025_condition'),
    ]

    operations = [
        migrations.CreateModel(
            name='socialmediaprofile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('platform', models.CharField(choices=[('linkedin', 'linkedin'), ('twitter', 'twitter'), ('facebook', 'facebook'), ('instagram', 'instagram')], max_length=20)),
                ('link', models.URLField(validators=[django.core.validators.URLValidator(message='Enter a valid URL.')])),
                ('team_member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='social_media_profiles', to='orbitor.team')),
            ],
        ),
    ]
