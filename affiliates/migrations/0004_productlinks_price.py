# Generated by Django 4.0.3 on 2022-03-12 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('affiliates', '0003_rename_link_adder_productlinks_influencer_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='productlinks',
            name='price',
            field=models.CharField(default=0, max_length=10),
        ),
    ]