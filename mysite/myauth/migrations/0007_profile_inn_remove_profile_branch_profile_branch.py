# Generated by Django 4.2.1 on 2023-05-23 09:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myauth', '0006_profile_id_alter_profile_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='inn',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='profile',
            name='branch',
        ),
        migrations.AddField(
            model_name='profile',
            name='branch',
            field=models.OneToOneField(default=2, on_delete=django.db.models.deletion.CASCADE, to='myauth.branch'),
            preserve_default=False,
        ),
    ]