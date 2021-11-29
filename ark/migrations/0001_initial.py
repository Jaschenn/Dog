# Generated by Django 3.2.9 on 2021-11-29 15:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Action',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_name', models.CharField(max_length=200)),
                ('action_type', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page_name', models.CharField(max_length=200)),
                ('technology_stack_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Release',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('release_datetime', models.DateTimeField()),
                ('release_status', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('extra', models.CharField(max_length=200)),
                ('action', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ark.action')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='triggered_on', to='ark.page')),
                ('released_at', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ark.release')),
                ('target', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jumps_to', to='ark.page')),
            ],
        ),
    ]