# Generated by Django 4.2.8 on 2024-02-17 19:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appMy', '0034_proimage_uyeler2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proimage',
            name='uyeler2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='appMy.uyeler'),
        ),
    ]
