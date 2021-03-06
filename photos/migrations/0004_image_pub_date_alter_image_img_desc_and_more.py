# Generated by Django 4.0.3 on 2022-03-26 14:14

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0003_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='image',
            name='img_desc',
            field=models.CharField(max_length=60),
        ),
        migrations.AlterField(
            model_name='image',
            name='img_name',
            field=models.CharField(max_length=60),
        ),
    ]
