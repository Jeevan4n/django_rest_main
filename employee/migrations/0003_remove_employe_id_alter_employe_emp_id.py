# Generated by Django 5.1.7 on 2025-03-09 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0002_alter_employe_emp_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employe',
            name='id',
        ),
        migrations.AlterField(
            model_name='employe',
            name='emp_id',
            field=models.CharField(max_length=20, primary_key=True, serialize=False, unique=True),
        ),
    ]
