# Generated by Django 5.1.7 on 2025-03-09 17:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0002_alter_employe_emp_id'),
        ('students', '0002_alter_student_roll'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='employe',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='employee.employe'),
        ),
    ]
