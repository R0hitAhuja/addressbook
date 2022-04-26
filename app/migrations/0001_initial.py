# Generated by Django 3.2 on 2021-04-24 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cust_id', models.IntegerField()),
                ('first_name', models.CharField(max_length=1000)),
                ('last_name', models.CharField(max_length=1000)),
                ('age', models.IntegerField()),
                ('sex', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=1000)),
                ('contactno', models.CharField(max_length=1000)),
            ],
        ),
    ]
