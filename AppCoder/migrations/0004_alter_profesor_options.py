# Generated by Django 4.0 on 2022-05-03 23:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0003_curso_alter_profesor_email'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profesor',
            options={'verbose_name': 'profesor', 'verbose_name_plural': 'profesores'},
        ),
    ]