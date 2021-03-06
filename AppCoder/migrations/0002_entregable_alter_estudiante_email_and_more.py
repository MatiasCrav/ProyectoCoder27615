# Generated by Django 4.0 on 2022-04-20 00:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Entregable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('fecha', models.DateField()),
                ('entrgado', models.BooleanField()),
            ],
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='profesor',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]
