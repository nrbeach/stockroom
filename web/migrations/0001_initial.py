# Generated by Django 4.2.1 on 2023-05-11 23:20

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.TextField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.TextField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Component',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('url', models.URLField(blank=True)),
                ('image', models.ImageField(blank=True, upload_to='')),
                ('description', models.TextField(max_length=255)),
                ('datasheet', models.URLField(blank=True)),
                ('mfn_pn', models.TextField(max_length=255)),
                ('count', models.IntegerField(default=1)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.category')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.location')),
            ],
        ),
    ]