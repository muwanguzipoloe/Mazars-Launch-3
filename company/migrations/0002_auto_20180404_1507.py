# Generated by Django 2.0.3 on 2018-04-04 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='info',
            old_name='response',
            new_name='comments',
        ),
        migrations.AlterField(
            model_name='info',
            name='status',
            field=models.CharField(blank=True, choices=[('Proposed', 'Proposed'), ('Contacted', 'Contacted'), ('Confirmed', 'Confirmed')], max_length=122, null=True),
        ),
        migrations.AlterField(
            model_name='info',
            name='telephone_contact',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
    ]