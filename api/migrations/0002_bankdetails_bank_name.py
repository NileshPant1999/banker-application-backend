# Generated by Django 3.1.4 on 2020-12-18 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bankdetails',
            name='bank_name',
            field=models.CharField(default='Central Bank Of India', max_length=60),
        ),
    ]
