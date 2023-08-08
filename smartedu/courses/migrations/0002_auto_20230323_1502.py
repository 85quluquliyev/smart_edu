# Generated by Django 3.2.7 on 2023-03-23 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='available',
            field=models.BooleanField(default=True, verbose_name='Geçerli'),
        ),
        migrations.AlterField(
            model_name='course',
            name='description',
            field=models.TextField(blank=True, help_text='Açıklama yazınız', null=True, verbose_name='Açıklama'),
        ),
        migrations.AlterField(
            model_name='course',
            name='image',
            field=models.ImageField(default='courses/dafault_course_image.jpg', upload_to='courses/%Y/%m/%d/', verbose_name='Resim'),
        ),
    ]