# Generated by Django 3.2 on 2022-01-04 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0010_alter_publication_job_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publication',
            name='author',
            field=models.IntegerField(verbose_name='Publication Author'),
        ),
    ]
