# Generated by Django 4.2.4 on 2023-09-11 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visit', '0004_migration_fo_formtype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formtype',
            name='info',
            field=models.CharField(blank=True, help_text='info', max_length=150, null=True, verbose_name='info'),
        ),
    ]
