# Generated by Django 3.2.6 on 2023-03-30 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0007_auto_20230330_2148'),
    ]

    operations = [
        migrations.AddField(
            model_name='entertainmentsplace',
            name='image',
            field=models.ImageField(default='test.txt', upload_to='entertainments-place-image/'),
            preserve_default=False,
        ),
    ]
