# Generated by Django 4.2 on 2025-04-27 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0010_alter_student_course_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='course_price',
            field=models.PositiveBigIntegerField(default=10000000),
        ),
    ]
