# Generated by Django 3.1.4 on 2020-12-25 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transfers',
            old_name='user',
            new_name='userId',
        ),
        migrations.AddField(
            model_name='transfers',
            name='amount',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]
