# Generated by Django 2.2.5 on 2019-09-10 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cosmetics', '0003_auto_20190910_1235'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='name',
        ),
        migrations.AddField(
            model_name='review',
            name='comment',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='review',
            name='title',
            field=models.CharField(blank=True, max_length=64),
        ),
    ]