# Generated by Django 4.2.8 on 2024-02-09 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appMy', '0009_alter_haberust1_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=50, verbose_name='Ad Soyad')),
                ('title', models.CharField(max_length=50, verbose_name='Konu')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('text', models.TextField(verbose_name='Mesaj')),
            ],
        ),
    ]
