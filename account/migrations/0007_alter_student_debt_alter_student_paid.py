# Generated by Django 4.2 on 2025-04-26 23:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_student_debt_student_is_debt_student_paid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='debt',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='paid',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
