# Generated by Django 3.2.6 on 2023-04-24 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0008_entertainmentsplace_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='foodplaces',
            name='reservable',
            field=models.BooleanField(default=False),
        ),
    ]
