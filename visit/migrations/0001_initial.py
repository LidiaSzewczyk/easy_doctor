# Generated by Django 4.2.4 on 2023-08-26 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Diagnosis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Utworzono')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Zmodyfikowano')),
                ('number', models.CharField(help_text='Numer', max_length=20, verbose_name='Numer')),
                ('name', models.CharField(help_text='Nazwa', max_length=250, verbose_name='Nazwa')),
                ('info', models.CharField(blank=True, help_text='Dodatkowe info', max_length=250, null=True, verbose_name='Dodatkowe info')),
                ('slug', models.SlugField(max_length=250, null=True, unique=True)),
            ],
            options={
                'verbose_name': 'Rozpoznanie',
                'verbose_name_plural': 'Rozpoznania',
            },
        ),
    ]
