# Generated by Django 3.0.4 on 2020-10-26 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voting', '0004_auto_20201026_1614'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foto',
            name='head_shot',
            field=models.ImageField(default='default.jpeg', upload_to='profil_images'),
        ),
    ]
