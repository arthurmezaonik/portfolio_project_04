# Generated by Django 3.2 on 2022-01-04 20:55

from django.db import migrations
import django.db.models.expressions


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0013_auto_20220104_2052'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='publication',
            options={'ordering': [django.db.models.expressions.OrderBy(django.db.models.expressions.F('author_fname'), nulls_last=True)]},
        ),
    ]
