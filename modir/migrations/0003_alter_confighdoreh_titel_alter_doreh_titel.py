# Generated by Django 4.2.3 on 2023-08-25 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modir', '0002_alter_doreh_titel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='confighdoreh',
            name='titel',
            field=models.CharField(max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='doreh',
            name='titel',
            field=models.CharField(max_length=6, null=True),
        ),
    ]
