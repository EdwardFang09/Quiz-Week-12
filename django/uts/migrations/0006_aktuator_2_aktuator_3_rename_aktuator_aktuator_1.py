# Generated by Django 4.2.1 on 2023-05-15 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uts', '0005_sistem1_sistem2_sistem3'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aktuator_2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('value', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Aktuator_3',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('value', models.CharField(max_length=200)),
            ],
        ),
        migrations.RenameModel(
            old_name='Aktuator',
            new_name='Aktuator_1',
        ),
    ]