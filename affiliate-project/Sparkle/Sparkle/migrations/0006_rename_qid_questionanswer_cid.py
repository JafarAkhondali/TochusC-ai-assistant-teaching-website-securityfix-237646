# Generated by Django 5.0.6 on 2024-06-14 12:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Sparkle', '0005_courseannouncement_courseassignment_coursequestion_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='questionanswer',
            old_name='qid',
            new_name='cid',
        ),
    ]
