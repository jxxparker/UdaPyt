# Generated by Django 4.0.1 on 2022-02-24 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0002_tag_review_project_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='vote_ratio',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='vote_total',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
