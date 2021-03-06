# Generated by Django 3.2.8 on 2021-12-19 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lunar', '0003_auto_20211212_0131'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(blank='True', default=' DEFAULT VALUE', max_length=200, null='True')),
                ('tutor', models.CharField(blank=True, max_length=200)),
                ('course_code', models.IntegerField()),
                ('venue', models.CharField(blank=True, max_length=200)),
                ('time', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Notifications',
        ),
    ]
