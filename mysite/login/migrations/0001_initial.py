# Generated by Django 2.2.7 on 2019-12-08 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=16)),
                ('password', models.CharField(max_length=160)),
                ('age', models.IntegerField()),
                ('create_time', models.DateField(auto_now_add=True)),
                ('update_time', models.DateField(auto_now=True)),
                ('enable', models.BooleanField(default=True)),
            ],
        ),
    ]
