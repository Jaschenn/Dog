# Generated by Django 3.2.9 on 2021-11-30 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ark', '0004_auto_20211130_0710'),
    ]

    operations = [
        migrations.AddField(
            model_name='release',
            name='release_events',
            field=models.ManyToManyField(blank=True, related_name='release_events', to='ark.Page'),
        ),
        migrations.AddField(
            model_name='release',
            name='release_pages',
            field=models.ManyToManyField(blank=True, related_name='release_pages', to='ark.Page'),
        ),
        migrations.RemoveField(
            model_name='page',
            name='page_screenshot',
        ),
        migrations.AddField(
            model_name='page',
            name='page_screenshot',
            field=models.ManyToManyField(blank=True, to='ark.Media'),
        ),
    ]
