# Generated by Django 2.2.2 on 2021-05-06 03:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('friends', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='friends',
            old_name='friend_email',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='friends',
            old_name='friend_f_name',
            new_name='f_name',
        ),
        migrations.RenameField(
            model_name='friends',
            old_name='friend_l_name',
            new_name='l_name',
        ),
        migrations.RenameField(
            model_name='friends',
            old_name='friend_number',
            new_name='number',
        ),
    ]
