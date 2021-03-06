# Generated by Django 3.0.6 on 2020-05-20 23:30

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0008_auto_20200520_1516'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='category',
            field=models.CharField(blank=True, choices=[('Web Design', 'webd'), ('Travel', 'travel'), ('Food', 'food'), ('Other', 'other')], default='webd', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='comments',
            name='comment_body',
            field=tinymce.models.HTMLField(),
        ),
    ]
