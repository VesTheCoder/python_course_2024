# Generated by Django 5.1.2 on 2024-10-19 16:29

import ckeditor.fields
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_event_galleryphoto_restaurantcontact_worker'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='restaurantcontact',
            name='address',
        ),
        migrations.RemoveField(
            model_name='restaurantcontact',
            name='email',
        ),
        migrations.RemoveField(
            model_name='restaurantcontact',
            name='opening_hours',
        ),
        migrations.RemoveField(
            model_name='restaurantcontact',
            name='phone',
        ),
        migrations.AddField(
            model_name='restaurantcontact',
            name='item_description',
            field=ckeditor.fields.RichTextField(default='lol'),
        ),
        migrations.AddField(
            model_name='restaurantcontact',
            name='item_icon',
            field=models.CharField(default='lol', max_length=250),
        ),
        migrations.AddField(
            model_name='restaurantcontact',
            name='item_title',
            field=models.CharField(default='lol', max_length=80),
        ),
        migrations.AlterField(
            model_name='dish',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='dishes', to='home.category'),
        ),
    ]
