# Generated by Django 4.1.2 on 2022-10-19 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('Email', models.EmailField(max_length=50)),
                ('Subject', models.CharField(max_length=50)),
                ('Message', models.CharField(max_length=150)),
            ],
        ),
    ]