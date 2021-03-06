# Generated by Django 3.0.7 on 2020-07-21 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='shoppingdetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uname', models.CharField(max_length=100)),
                ('uHname', models.CharField(max_length=100)),
                ('uemail', models.EmailField(max_length=100)),
                ('umob', models.CharField(max_length=15)),
                ('upostoffice', models.CharField(max_length=200)),
                ('ulandmark', models.CharField(max_length=200)),
                ('upin', models.IntegerField()),
                ('ucity', models.CharField(max_length=200)),
                ('udistrict', models.CharField(max_length=100)),
                ('ustate', models.CharField(max_length=100)),
                ('ucountry', models.CharField(max_length=100)),
                ('quantity', models.IntegerField()),
                ('pid', models.IntegerField()),
                ('status', models.BooleanField(default=False)),
                ('price', models.FloatField()),
                ('code', models.CharField(max_length=100)),
                ('delivery', models.BooleanField(default=False)),
                ('tracking', models.CharField(max_length=200)),
            ],
        ),
    ]
