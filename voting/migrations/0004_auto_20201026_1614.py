# Generated by Django 3.0.4 on 2020-10-26 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voting', '0003_auto_20201026_1609'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foto',
            name='head_shot',
            field=models.ImageField(blank=True, default='Media/default.jpeg', upload_to='profil_images'),
        ),
    ]