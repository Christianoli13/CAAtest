# Generated by Django 2.0.4 on 2018-04-22 05:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('caa', '0009_auto_20180422_0229'),
    ]

    operations = [
        migrations.RenameField(
            model_name='respostas',
            old_name='curso',
            new_name='Curso',
        ),
    ]