# Generated by Django 4.2.3 on 2023-09-12 16:24

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orbitor', '0015_remove_blog_head2_remove_blog_head3_alter_blog_head1_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectdetail',
            name='url',
            field=models.URLField(default=0, validators=[django.core.validators.URLValidator(message='Enter a valid URL.')]),
            preserve_default=False,
        ),
    ]
