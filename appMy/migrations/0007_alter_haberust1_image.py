# Generated by Django 4.2.8 on 2024-02-07 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appMy', '0006_haberust1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='haberust1',
            name='image',
            field=models.ImageField(max_length=250, upload_to='img', verbose_name='Haber Resmi'),
        ),
    ]