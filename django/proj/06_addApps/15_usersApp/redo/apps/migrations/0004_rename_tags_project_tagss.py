# Generated by Django 4.0.1 on 2022-03-15 21:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0003_tag_project_tags'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='tags',
            new_name='tagss',
        ),
    ]
