# Generated by Django 4.1.6 on 2023-02-08 19:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('moodle', '0006_alter_professor_departamento'),
    ]

    operations = [
        migrations.AddField(
            model_name='prova',
            name='professor',
            field=models.OneToOneField(default=2, on_delete=django.db.models.deletion.CASCADE, to='moodle.professor'),
            preserve_default=False,
        ),
    ]
