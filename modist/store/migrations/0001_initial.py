# Generated by Django 3.1 on 2020-10-19 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='pics')),
                ('description', models.CharField(max_length=70)),
                ('price', models.FloatField()),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Testimony',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='pics')),
                ('testimony', models.TextField()),
                ('name', models.CharField(max_length=30)),
                ('position', models.CharField(choices=[('C', 'Customer'), ('S', 'Staff')], max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='TrendingProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='pics')),
                ('status', models.IntegerField(default=False)),
                ('description', models.CharField(max_length=70)),
                ('old_price', models.FloatField()),
                ('new_price', models.FloatField()),
                ('name', models.CharField(max_length=20)),
            ],
        ),
    ]
