# Generated by Django 2.0.4 on 2018-05-10 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0003_auto_20180404_1543'),
    ]

    operations = [
        migrations.AddField(
            model_name='invitees',
            name='category',
            field=models.CharField(blank=True, choices=[('Regulator', 'Regulator'), ('Current client', 'Current client'), ('Prospective client', 'Prospective client'), ('Diplomatic Co.', 'Diplomatic Co.'), ('Mazars group', 'Mazars group'), ('Others', 'Others')], max_length=122, null=True),
        ),
    ]