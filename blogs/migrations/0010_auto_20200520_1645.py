# Generated by Django 3.0.6 on 2020-05-20 23:45

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0009_auto_20200520_1630'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='content',
            field=tinymce.models.HTMLField(verbose_name='Content'),
        ),
    ]
