# Generated by Django 4.1.6 on 2023-02-08 19:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('moodle', '0005_questao_professor_alter_questao_departamento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='professor',
            name='departamento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='moodle.departamento'),
        ),
    ]
