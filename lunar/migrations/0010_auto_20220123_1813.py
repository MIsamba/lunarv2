# Generated by Django 3.2.8 on 2022-01-23 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lunar', '0009_session_phone_no'),
    ]

    operations = [
        migrations.RenameField(
            model_name='posts',
            old_name='image',
            new_name='avater',
        ),
        migrations.AddField(
            model_name='posts',
            name='name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='posts',
            name='photo',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
