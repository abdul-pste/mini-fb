# Generated by Django 5.1.1 on 2024-10-28 18:31

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mini_fb', '0003_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='city',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='profile',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='profile',
            name='first_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='profile',
            name='last_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='statusmessage',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mini_fb.profile'),
        ),
        migrations.AlterField(
            model_name='statusmessage',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.CreateModel(
            name='Friend',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('profile1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='profile1', to='mini_fb.profile')),
                ('profile2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='profile2', to='mini_fb.profile')),
            ],
        ),
    ]