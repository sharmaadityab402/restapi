# Generated by Django 3.0.4 on 2020-03-11 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Employee_code', models.CharField(max_length=100000, unique=True)),
                ('Department', models.CharField(max_length=100)),
                ('Score', models.IntegerField()),
                ('Date_Created', models.DateTimeField()),
            ],
        ),
    ]
