# Generated by Django 2.0.4 on 2018-04-21 21:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('caa', '0003_auto_20180421_1345'),
    ]

    operations = [
        migrations.CreateModel(
            name='cursos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('curso', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='disciplina',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150)),
                ('código', models.CharField(max_length=150)),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='caa.cursos')),
            ],
        ),
        migrations.CreateModel(
            name='respostas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Resposta1', models.CharField(max_length=150)),
                ('Resposta2', models.CharField(max_length=150)),
                ('Resposta3', models.CharField(max_length=150)),
                ('Resposta4', models.CharField(max_length=150)),
                ('Resposta5', models.CharField(max_length=150)),
                ('Resposta6', models.CharField(max_length=150)),
                ('Resposta7', models.CharField(max_length=150)),
                ('Resposta8', models.CharField(max_length=150)),
                ('Resposta9', models.CharField(max_length=150)),
                ('Resposta10', models.CharField(max_length=150)),
                ('Resposta11', models.CharField(max_length=150)),
                ('Resposta12', models.CharField(max_length=150)),
                ('Resposta13', models.CharField(max_length=150)),
                ('Resposta14', models.CharField(max_length=150)),
                ('Resposta15', models.CharField(max_length=150)),
                ('Resposta16', models.CharField(max_length=150)),
                ('Resposta17', models.CharField(max_length=150)),
                ('Resposta18', models.CharField(max_length=150)),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='caa.cursos')),
                ('código', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='caa.disciplina')),
                ('nome', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='caa.dadosaluno')),
            ],
        ),
    ]
