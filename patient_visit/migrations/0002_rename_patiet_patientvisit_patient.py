# Generated by Django 4.2.4 on 2023-09-01 09:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patient_visit', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='patientvisit',
            old_name='patiet',
            new_name='patient',
        ),
    ]