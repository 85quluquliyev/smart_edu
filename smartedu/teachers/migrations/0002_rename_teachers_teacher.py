# Generated by Django 3.2.7 on 2023-03-27 14:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0008_course_teacher'),
        ('teachers', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Teachers',
            new_name='Teacher',
        ),
    ]
