# Generated by Django 5.0.3 on 2024-03-17 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('searchmeds', '0005_alter_medprofile_apresentacao_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medprofile',
            name='apresentacao',
            field=models.CharField(max_length=10000, null=True),
        ),
        migrations.AlterField(
            model_name='medprofile',
            name='classe_terapeutica',
            field=models.CharField(max_length=10000, null=True),
        ),
        migrations.AlterField(
            model_name='medprofile',
            name='laboratorio',
            field=models.CharField(max_length=10000, null=True),
        ),
        migrations.AlterField(
            model_name='medprofile',
            name='produto',
            field=models.CharField(max_length=10000, null=True),
        ),
        migrations.AlterField(
            model_name='medprofile',
            name='regime_de_preco',
            field=models.CharField(max_length=10000, null=True),
        ),
        migrations.AlterField(
            model_name='medprofile',
            name='substancia',
            field=models.CharField(max_length=10000, null=True),
        ),
        migrations.AlterField(
            model_name='medprofile',
            name='tipo_de_produto',
            field=models.CharField(max_length=10000, null=True),
        ),
    ]