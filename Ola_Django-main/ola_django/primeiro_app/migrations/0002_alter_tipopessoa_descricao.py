# Generated by Django 5.1.2 on 2024-10-21 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('primeiro_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tipopessoa',
            name='descricao',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
    ]