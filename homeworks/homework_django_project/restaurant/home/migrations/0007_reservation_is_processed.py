# Generated by Django 5.1.2 on 2024-10-20 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_worker_facebook_worker_instagram_worker_linkedin_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='is_processed',
            field=models.BooleanField(default=False),
        ),
    ]
