# Generated by Django 4.1.7 on 2023-03-23 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_alter_course_available_alter_course_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='image',
            field=models.ImageField(default='courses/default_course_image.jpg', upload_to='courses/%Y/%m/%d/'),
        ),
    ]
