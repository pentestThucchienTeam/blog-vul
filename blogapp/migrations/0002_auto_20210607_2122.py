# Generated by Django 3.2.4 on 2021-06-07 14:22

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(default=''),
        ),
        migrations.AlterField(
            model_name='vul',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]