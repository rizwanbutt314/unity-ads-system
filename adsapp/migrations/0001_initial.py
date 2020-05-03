# Generated by Django 2.1.5 on 2020-05-03 12:22

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdsData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bundle_id', models.CharField(blank=True, help_text='Bundle ID', max_length=255, null=True)),
                ('active', models.BooleanField(default=False)),
                ('hit_link', models.TextField(help_text='Hit link', max_length=255)),
                ('ready', models.BooleanField(default=False)),
                ('photo', models.ImageField(storage=django.core.files.storage.FileSystemStorage(base_url='/media/', location='/home/rizwan/Desktop/heroku_apps/unity-ads-system/MEDIA'), upload_to='photos')),
                ('uploaded_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
