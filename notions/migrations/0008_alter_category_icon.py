# Generated by Django 4.0.2 on 2022-03-21 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notions', '0007_remove_link_icon_category_icon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='icon',
            field=models.ImageField(blank=True, upload_to='media/'),
        ),
    ]