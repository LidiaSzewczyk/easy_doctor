# Generated by Django 4.2.4 on 2023-08-30 08:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Utworzono')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Zmodyfikowano')),
                ('first_name', models.CharField(help_text='imię', max_length=150, verbose_name='imię')),
                ('last_name', models.CharField(help_text='nazwisko', max_length=150, verbose_name='nazwisko')),
                ('email', models.EmailField(help_text='email', max_length=254, verbose_name='email')),
                ('birth_date', models.DateField(help_text='Data urodzenia', verbose_name='Data urodzenia')),
                ('address', models.CharField(help_text='adres', max_length=250, verbose_name='adres')),
                ('pesel', models.CharField(help_text='PESEL', max_length=20, verbose_name='PESEL')),
                ('phone', models.CharField(blank=True, help_text='Tel.', max_length=15, null=True, verbose_name='Tel.')),
                ('doctor', models.ForeignKey(help_text='lekarz', on_delete=django.db.models.deletion.CASCADE, related_name='patients', to=settings.AUTH_USER_MODEL, verbose_name='lekarz')),
            ],
            options={
                'verbose_name': 'pacjent',
                'verbose_name_plural': 'pacjenci',
            },
        ),
    ]
