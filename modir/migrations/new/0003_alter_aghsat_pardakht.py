# Generated by Django 4.2.3 on 2023-07-27 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modir', '0002_alter_aghsat_tarikh'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aghsat',
            name='pardakht',
            field=models.DateField(blank=True),
        ),
    ]
