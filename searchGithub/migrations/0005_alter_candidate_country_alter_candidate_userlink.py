# Generated by Django 4.1.1 on 2022-09-24 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('searchGithub', '0004_alter_candidate_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='country',
            field=models.CharField(max_length=80),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='userLink',
            field=models.CharField(max_length=150),
        ),
    ]