# Generated by Django 4.2.3 on 2023-08-12 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modir', '0012_alter_aghsat_pardakht'),
    ]

    operations = [
        migrations.CreateModel(
            name='MSandogh',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mojodi', models.BigIntegerField()),
            ],
        ),
    ]
