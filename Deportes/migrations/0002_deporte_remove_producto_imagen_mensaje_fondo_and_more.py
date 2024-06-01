# Generated by Django 5.0.6 on 2024-05-31 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Deportes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Deporte',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(blank=True, default='/Deportes/media/deporte.jpeg', null=True, upload_to='imagenes')),
                ('nombre', models.CharField(max_length=200)),
                ('descripcion', models.CharField(max_length=300)),
            ],
        ),
        migrations.RemoveField(
            model_name='producto',
            name='imagen',
        ),
        migrations.AddField(
            model_name='mensaje',
            name='fondo',
            field=models.ImageField(blank=True, default='/Deportes/media/encabesado.jpeg', null=True, upload_to='imagenes'),
        ),
        migrations.AddField(
            model_name='mensaje',
            name='subtitulo',
            field=models.CharField(default='¡Encuentra todo lo que necesita para mentenerte activo!', max_length=200),
        ),
        migrations.AddField(
            model_name='producto',
            name='imagen1',
            field=models.ImageField(blank=True, default='/Deportes/media/estadio1.jpeg', null=True, upload_to='imagenes'),
        ),
        migrations.AddField(
            model_name='producto',
            name='imagen2',
            field=models.ImageField(blank=True, default='/Deportes/media/estadio2.jpeg', null=True, upload_to='imagenes'),
        ),
        migrations.AddField(
            model_name='producto',
            name='imagen3',
            field=models.ImageField(blank=True, default='/Deportes/media/estadio3.jpeg', null=True, upload_to='imagenes'),
        ),
        migrations.AddField(
            model_name='producto',
            name='imagen4',
            field=models.ImageField(blank=True, default='/Deportes/media/estadio4.jpeg', null=True, upload_to='imagenes'),
        ),
        migrations.AlterField(
            model_name='mensaje',
            name='msj',
            field=models.CharField(default='Landing Page Deportes', max_length=200),
        ),
    ]
