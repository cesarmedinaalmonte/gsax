# Generated by Django 2.1.3 on 2018-12-08 17:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('GestionAcademica', '0006_auto_20181208_0321'),
    ]

    operations = [
        migrations.AddField(
            model_name='materia',
            name='Profesor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='GestionAcademica.Docente'),
        ),
    ]