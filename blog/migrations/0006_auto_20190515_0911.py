# Generated by Django 2.2 on 2019-05-15 09:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_remove_authors_articles'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Authors',
            new_name='Author',
        ),
    ]
