# Generated by Django 4.0.1 on 2022-03-23 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0007_project_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='featured_image',
            field=models.ImageField(blank=True, default='user-default.png', null=True, upload_to=''),
        ),
    ]