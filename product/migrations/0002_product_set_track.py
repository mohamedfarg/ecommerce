# Generated by Django 4.0.3 on 2023-08-29 23:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='set_track',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
