# Generated by Django 3.0.5 on 2020-04-18 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20200418_1601'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='slug',
            field=models.SlugField(blank=True, max_length=264, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(blank=True, max_length=100, null=True, unique='True'),
        ),
    ]
