# Generated by Django 4.2.1 on 2023-05-23 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myauth', '0007_profile_inn_remove_profile_branch_profile_branch'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='branch',
        ),
        migrations.AddField(
            model_name='profile',
            name='branch',
            field=models.ManyToManyField(to='myauth.branch'),
        ),
    ]