# Generated by Django 3.0.7 on 2020-07-14 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myfinance', '0009_auto_20200714_0407'),
    ]

    operations = [
        migrations.AlterField(
            model_name='despesa',
            name='classificacao',
            field=models.CharField(max_length=255),
        ),
    ]