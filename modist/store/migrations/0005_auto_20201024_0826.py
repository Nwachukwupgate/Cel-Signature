# Generated by Django 3.1 on 2020-10-24 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_shop'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop',
            name='status',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
