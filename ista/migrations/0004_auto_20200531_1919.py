# Generated by Django 2.1.7 on 2020-05-31 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ista', '0003_auto_20200531_1806'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment',
            field=models.TextField(blank=True, null=True),
        ),
    ]
