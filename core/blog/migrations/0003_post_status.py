# Generated by Django 3.2.19 on 2023-05-18 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_rename_blog_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='status',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]