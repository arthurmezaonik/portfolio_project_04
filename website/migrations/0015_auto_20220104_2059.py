# Generated by Django 3.2 on 2022-01-04 20:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0014_alter_publication_options'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='job',
            new_name='publication',
        ),
        migrations.RemoveField(
            model_name='publication',
            name='slug',
        ),
    ]