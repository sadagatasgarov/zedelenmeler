# Generated by Django 4.2.4 on 2023-08-08 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sahbuz', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ats',
            name='adi',
            field=models.CharField(max_length=30, null=True, unique=True, verbose_name='Adı'),
        ),
        migrations.AlterField(
            model_name='idare',
            name='adi',
            field=models.CharField(max_length=50, null=True, verbose_name='İdarənin adı'),
        ),
        migrations.AlterField(
            model_name='komekcipaylayiciskafdakikabelnomreleri',
            name='kskafdaki_kabelin_nomresi',
            field=models.CharField(max_length=10, null=True, unique=True, verbose_name='Köməkçi paylayıcı şkafdaki kabel nömrəsi'),
        ),
        migrations.AlterField(
            model_name='montyor',
            name='adi',
            field=models.CharField(max_length=30, null=True, verbose_name='Adı'),
        ),
        migrations.AlterField(
            model_name='nomreler',
            name='nomre',
            field=models.CharField(max_length=11, unique=True, verbose_name='Nömrə'),
        ),
        migrations.AlterField(
            model_name='paylayiciskafdakikabelnomreleri',
            name='kabelin_nomresi',
            field=models.CharField(max_length=10, null=True, unique=True, verbose_name='Kabelin nömrəsi'),
        ),
    ]
