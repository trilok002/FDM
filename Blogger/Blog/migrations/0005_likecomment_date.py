# Generated by Django 3.0 on 2020-01-10 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0004_auto_20200110_1550'),
    ]

    operations = [
        migrations.AddField(
            model_name='likecomment',
            name='date',
            field=models.DateField(null=True),
        ),
    ]
