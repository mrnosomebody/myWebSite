# Generated by Django 4.0.2 on 2022-03-21 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notions', '0005_remove_link_icon_category_icon'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='icon',
        ),
        migrations.AddField(
            model_name='link',
            name='icon',
            field=models.ImageField(default='', upload_to='media/'),
            preserve_default=False,
        ),
    ]
