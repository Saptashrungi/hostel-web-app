# Generated by Django 3.0.8 on 2020-11-26 11:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hostel_webapp', '0005_student_avatar'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='complaint',
            name='complaint_pic',
        ),
    ]