# Generated by Django 4.2.4 on 2023-08-08 12:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Kengerli', '0003_alter_olculmuszedeninxususiyyeti_sebeb_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zedelenmelerinqeydiyyatijurnali',
            name='operator',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Kengerli_ZedelenmelerinQeydiyyatiJurnali', to=settings.AUTH_USER_MODEL, verbose_name='Qeydə alan'),
        ),
        migrations.AlterField(
            model_name='zedelenmelerinqeydiyyatijurnali',
            name='operator2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Kengerli_ZedelenmelerinQeydiyyatiJurnali2', to=settings.AUTH_USER_MODEL, verbose_name='Sonuncu defe düzəliş edən'),
        ),
    ]
