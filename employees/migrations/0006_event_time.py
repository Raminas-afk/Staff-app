# Generated by Django 4.1.3 on 2022-12-05 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0005_alter_event_attending_department_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='time',
            field=models.TimeField(default="00:00"),
            preserve_default=False,
        ),
    ]
