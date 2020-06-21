# Generated by Django 3.0.7 on 2020-06-19 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
                ('birth', models.PositiveIntegerField(null=True)),
                ('city', models.CharField(max_length=50, null=True)),
                ('gender', models.BooleanField(null=True)),
                ('chatId', models.IntegerField(null=True)),
                ('last_name', models.CharField(max_length=30, null=True)),
            ],
        ),
    ]
