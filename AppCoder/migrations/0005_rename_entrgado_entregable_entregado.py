# Generated by Django 4.0 on 2022-05-04 00:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0004_alter_profesor_options'),
    ]

    operations = [
        migrations.RenameField(
            model_name='entregable',
            old_name='entrgado',
            new_name='entregado',
        ),
    ]
