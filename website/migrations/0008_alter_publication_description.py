# Generated by Django 3.2 on 2022-01-01 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0007_auto_20220101_2139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publication',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
