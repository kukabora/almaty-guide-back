# Generated by Django 3.2.6 on 2023-04-25 11:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0012_menutype'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menutype',
            name='menu',
        ),
        migrations.AddField(
            model_name='menu',
            name='menu_type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='mainapp.menutype'),
            preserve_default=False,
        ),
    ]