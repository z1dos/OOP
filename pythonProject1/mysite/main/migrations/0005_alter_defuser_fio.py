# Generated by Django 3.2.9 on 2021-12-09 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20211209_0953'),
    ]

    operations = [
        migrations.AlterField(
            model_name='defuser',
            name='fio',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='ФИО'),
        ),
    ]
