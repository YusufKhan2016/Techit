# Generated by Django 4.2.3 on 2023-11-02 06:11

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orbitor', '0032_faq'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faq',
            name='ans',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
        migrations.AlterField(
            model_name='faq',
            name='quest',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]
