# Generated by Django 4.2.4 on 2023-09-11 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visit', '0002_formtype_part_text_priority_choice'),
    ]

    operations = [
        migrations.AddField(
            model_name='formtype',
            name='info',
            field=models.CharField(blank=True, help_text='nazwa', max_length=150, null=True, verbose_name='nazwa'),
        ),
    ]
