# Generated by Django 5.0 on 2023-12-12 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_alter_chat_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='characters/'),
        ),
    ]