# Generated by Django 2.2 on 2019-05-13 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='Bio',
            field=models.TextField(),
        ),
    ]
