# Generated by Django 4.1.4 on 2022-12-13 20:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0002_remove_attendance_course_remove_attendance_section_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='random',
        ),
    ]