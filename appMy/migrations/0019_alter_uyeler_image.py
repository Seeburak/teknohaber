# Generated by Django 4.2.8 on 2024-02-15 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appMy', '0018_uyeler_gizlisoru'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uyeler',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Haber Resmi'),
        ),
    ]
