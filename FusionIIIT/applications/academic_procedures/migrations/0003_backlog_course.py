# Generated by Django 3.1.5 on 2024-02-18 18:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('programme_curriculum', '0002_auto_20240217_1700'),
        ('academic_information', '0001_initial'),
        ('academic_procedures', '0002_auto_20240217_1700'),
    ]

    operations = [
        migrations.CreateModel(
            name='backlog_course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_summer_course', models.BooleanField(default=False)),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academic_information.course')),
                ('semester_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='programme_curriculum.semester')),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academic_information.student')),
            ],
        ),
    ]
