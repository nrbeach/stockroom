# Generated by Django 4.2.1 on 2023-05-11 23:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='component',
            name='name',
            field=models.TextField(default='Unnamed', max_length=255),
            preserve_default=False,
        ),
    ]
