# Generated by Django 4.0.6 on 2024-06-06 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_alter_order_profit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='cateImage',
            field=models.ImageField(blank=True, null=True, upload_to='cate_img/', verbose_name='Category Image'),
        ),
    ]
