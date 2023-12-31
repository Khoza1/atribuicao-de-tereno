# Generated by Django 3.2 on 2023-10-30 20:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RecursoNatural',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('quantidade', models.FloatField()),
                ('tipo', models.CharField(max_length=100)),
                ('localizacao', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Terreno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('proprietario', models.CharField(max_length=100)),
                ('limites_propriedade', models.TextField()),
                ('uso_da_terra', models.CharField(max_length=100)),
                ('historico_transacoes', models.TextField()),
                ('localizacao', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Documento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=100)),
                ('arquivo', models.FileField(upload_to='documentos/')),
                ('terreno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='timapp.terreno')),
            ],
        ),
    ]
