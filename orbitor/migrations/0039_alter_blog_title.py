# Generated by Django 4.2.3 on 2023-11-25 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orbitor', '0038_remove_blog_head0'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
