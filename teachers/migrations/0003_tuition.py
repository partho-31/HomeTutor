# Generated by Django 5.1.7 on 2025-03-24 09:09

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0002_alter_teacher_managers_remove_teacher_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tuition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('description', models.TextField()),
                ('classes', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('subjects', models.CharField(max_length=150)),
                ('availability', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='Yes', max_length=5)),
                ('Enrolled', models.PositiveIntegerField(default=0)),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tuiton', to='teachers.teacher')),
            ],
        ),
    ]
