# Generated by Django 4.1.4 on 2022-12-12 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='indicators',
            name='link',
            field=models.URLField(blank=True, max_length=500, null=True),
        ),
    ]