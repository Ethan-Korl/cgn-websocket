# Generated by Django 5.0.4 on 2024-04-22 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='phone',
            field=models.CharField(default=1, max_length=10, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='customuser',
            name='username',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
