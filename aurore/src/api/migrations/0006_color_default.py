# Generated by Django 3.0.5 on 2020-07-11 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20200612_1150'),
    ]

    operations = [
        migrations.AddField(
            model_name='color',
            name='default',
            field=models.BooleanField(default=False),
        ),
    ]