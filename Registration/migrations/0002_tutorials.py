# Generated by Django 3.0.7 on 2021-06-20 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Registration', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tutorials',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=100)),
                ('code', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
                ('link', models.CharField(max_length=1000)),
            ],
        ),
    ]
