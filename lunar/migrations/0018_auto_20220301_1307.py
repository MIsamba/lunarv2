# Generated by Django 3.2.8 on 2022-03-01 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lunar', '0017_auto_20220227_1542'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hero',
            name='alias',
            field=models.CharField(max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='hero',
            name='name',
            field=models.CharField(max_length=60, null=True),
        ),
    ]
