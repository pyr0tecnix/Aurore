# Generated by Django 3.0.5 on 2020-06-12 11:47

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20200612_1103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alarm',
            name='days',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='alarm',
            name='task_id',
            field=models.UUIDField(default=uuid.UUID('8ce9de56-aca2-11ea-81de-0242ac130006'), unique=True),
        ),
    ]
