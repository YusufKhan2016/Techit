# Generated by Django 4.2.3 on 2023-11-11 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orbitor', '0034_delete_award_remove_logoslider_height_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='logo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.ImageField(upload_to='pics')),
                ('logo', models.ImageField(upload_to='pics')),
            ],
        ),
    ]