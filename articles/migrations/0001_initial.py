# Generated by Django 3.2.3 on 2021-06-04 23:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source_id', models.CharField(blank=True, max_length=64)),
                ('source_name', models.CharField(max_length=64)),
                ('author', models.CharField(max_length=64)),
                ('title', models.CharField(max_length=128)),
                ('description', models.TextField()),
                ('url', models.CharField(max_length=256)),
                ('url_to_image', models.CharField(max_length=256)),
                ('published_at', models.DateTimeField()),
                ('content', models.TextField()),
            ],
        ),
    ]
