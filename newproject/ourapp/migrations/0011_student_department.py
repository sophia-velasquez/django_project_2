# Generated by Django 3.2.2 on 2021-05-12 19:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ourapp', '0010_remove_student_department'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='department',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='ourapp.department'),
            preserve_default=False,
        ),
    ]
