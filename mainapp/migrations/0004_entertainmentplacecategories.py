# Generated by Django 3.2.6 on 2023-03-30 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_auto_20230329_1613'),
    ]

    operations = [
        migrations.CreateModel(
            name='EntertainmentPlaceCategories',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('category_name', models.CharField(max_length=50)),
            ],
        ),
    ]
