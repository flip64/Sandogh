# Generated by Django 4.2.3 on 2023-08-11 19:00

from django.db import migrations
import django_jalali.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('modir', '0009_alter_loan_tarikh'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aghsat',
            name='tarikh',
            field=django_jalali.db.models.jDateField(),
        ),
    ]