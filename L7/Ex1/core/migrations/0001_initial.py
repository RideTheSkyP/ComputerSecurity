# Generated by Django 3.1.4 on 2020-12-25 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Transfers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=100)),
                ('transferFrom', models.IntegerField()),
                ('transferTo', models.IntegerField()),
            ],
        ),
    ]
