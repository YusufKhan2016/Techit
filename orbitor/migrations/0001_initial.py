# Generated by Django 4.1.7 on 2023-06-04 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='sevices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('img', models.ImageField(upload_to='pics')),
                ('Desc', models.TextField()),
            ],
        ),
    ]
