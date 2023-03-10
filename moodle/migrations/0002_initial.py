# Generated by Django 4.1.6 on 2023-02-08 03:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('moodle', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='professor',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='inscricao',
            name='aluno',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='moodle.aluno'),
        ),
        migrations.AddField(
            model_name='inscricao',
            name='disciplina',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='moodle.disciplina'),
        ),
        migrations.AddField(
            model_name='disciplina',
            name='aluno',
            field=models.ManyToManyField(through='moodle.Inscricao', to='moodle.aluno'),
        ),
        migrations.AddField(
            model_name='disciplina',
            name='professor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='moodle.professor'),
        ),
        migrations.AddField(
            model_name='desempenho',
            name='aluno',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='moodle.aluno'),
        ),
        migrations.AddField(
            model_name='desempenho',
            name='prova',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='moodle.prova'),
        ),
        migrations.AddField(
            model_name='cadernoresposta',
            name='desempenho',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='moodle.desempenho'),
        ),
        migrations.AddField(
            model_name='cadernoresposta',
            name='questao',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='moodle.questao'),
        ),
        migrations.AddField(
            model_name='aluno',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='alternativa',
            name='questao',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='moodle.questao'),
        ),
    ]
