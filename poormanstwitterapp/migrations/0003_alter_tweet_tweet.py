# Generated by Django 3.2.6 on 2021-08-16 23:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poormanstwitterapp', '0002_alter_tweet_tweet'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='tweet',
            field=models.CharField(max_length=50),
        ),
    ]