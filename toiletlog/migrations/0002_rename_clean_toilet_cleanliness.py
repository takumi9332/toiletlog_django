# Generated by Django 3.2.8 on 2021-11-05 23:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('toiletlog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='toilet',
            old_name='clean',
            new_name='cleanliness',
        ),
    ]