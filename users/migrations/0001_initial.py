# Generated by Django 4.0.2 on 2022-03-07 09:21

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='Category')),
                ('slug', models.SlugField()),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='users.category', verbose_name='Parent category')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='LinksList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name="What's there")),
                ('url', models.URLField(max_length=510, verbose_name='Link')),
                ('category', mptt.fields.TreeForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='links', to='users.category', verbose_name='Category')),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('wallet_address', models.CharField(blank=True, max_length=255, verbose_name='Wallet address')),
                ('links_list', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='users.linkslist')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
