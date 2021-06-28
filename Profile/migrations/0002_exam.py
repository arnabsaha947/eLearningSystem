# Generated by Django 3.0.7 on 2021-06-22 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=100)),
                ('ecode', models.CharField(max_length=100)),
                ('questions', models.CharField(max_length=1000)),
                ('options_a', models.CharField(max_length=100)),
                ('options_b', models.CharField(max_length=100)),
                ('options_c', models.CharField(max_length=100)),
                ('options_d', models.CharField(max_length=100)),
                ('answers', models.CharField(max_length=100)),
            ],
        ),
    ]
