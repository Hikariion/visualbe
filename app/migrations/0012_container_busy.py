# Generated by Django 3.2.12 on 2022-05-22 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_alter_task_node_wait_start_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='container',
            name='busy',
            field=models.BooleanField(default=0),
            preserve_default=False,
        ),
    ]
