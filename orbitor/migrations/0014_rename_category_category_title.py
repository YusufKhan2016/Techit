# Generated by Django 4.2.3 on 2023-09-07 12:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orbitor', '0013_services_delete_sevices'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='category',
            new_name='title',
        ),
    ]
