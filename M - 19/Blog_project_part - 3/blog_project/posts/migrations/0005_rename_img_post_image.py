# Generated by Django 5.0.4 on 2024-06-29 08:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_alter_post_img'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='img',
            new_name='image',
        ),
    ]
