# Generated by Django 3.2.8 on 2021-10-31 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Classes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_name', models.CharField(blank=True, max_length=200, null=True)),
                ('class_code', models.IntegerField()),
                ('class_assignments_written', models.CharField(blank=True, max_length=200, null=True)),
                ('class_assignment_image', models.ImageField(blank=True, default='/placeholder.png', null=True, upload_to='')),
                ('class_attendance', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_code', models.IntegerField()),
                ('course_name', models.CharField(blank=True, max_length=200, null=True)),
                ('course_class', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('student_id', models.IntegerField()),
                ('student_group', models.CharField(blank=True, max_length=200, null=True)),
                ('student_name', models.CharField(blank=True, max_length=200, null=True)),
                ('student_class_code', models.IntegerField(blank=True, default=0, null=True)),
                ('student_total', models.IntegerField(blank=True, default=0, null=True)),
                ('_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
            ],
        ),
    ]
