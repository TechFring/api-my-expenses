# Generated by Django 3.2.5 on 2021-08-10 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'categories'},
        ),
        migrations.AlterField(
            model_name='expense',
            name='description',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
