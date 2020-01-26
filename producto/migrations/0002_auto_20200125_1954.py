# Generated by Django 3.0.2 on 2020-01-25 23:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='descripcion',
            field=models.TextField(blank=True, help_text='Ingrese Descripción del prodcuto', max_length=100, verbose_name='Descripcion:'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='imagen',
            field=models.CharField(help_text='Ingrese URL de la imagen', max_length=100, verbose_name='Imagen Producto:'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='nombre',
            field=models.DateField(help_text='Ingrese URL de la imagen', verbose_name='Vencimiento:'),
        ),
    ]
