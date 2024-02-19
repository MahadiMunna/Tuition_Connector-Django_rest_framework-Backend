# Generated by Django 5.0.1 on 2024-02-18 15:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tuitions', '0002_alter_studentclass_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tuition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medium', models.CharField(choices=[('Bangla', 'Bangla'), ('English', 'English')], max_length=10)),
                ('tuition_type', models.CharField(choices=[('Online', 'Online'), ('Offline', 'Offline')], max_length=10)),
                ('location', models.CharField(max_length=100)),
                ('tuition_details', models.TextField()),
                ('time', models.CharField(max_length=20)),
                ('salary', models.DecimalField(decimal_places=2, max_digits=10)),
                ('availability', models.BooleanField(default=True)),
                ('student_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tuitions.studentclass')),
                ('subject', models.ManyToManyField(to='tuitions.subject')),
            ],
        ),
        migrations.DeleteModel(
            name='Tution',
        ),
    ]