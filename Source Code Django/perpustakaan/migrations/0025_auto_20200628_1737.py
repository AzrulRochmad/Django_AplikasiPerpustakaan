# Generated by Django 2.2.12 on 2020-06-28 17:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('perpustakaan', '0024_auto_20200628_1733'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='buku',
            name='cover',
        ),
        migrations.RemoveField(
            model_name='buku',
            name='tanggal',
        ),
    ]