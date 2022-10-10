# Generated by Django 4.1 on 2022-09-25 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_delete_blogcategory'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='category',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='blog',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]