# Generated by Django 2.2 on 2021-07-13 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_item_discount_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='description',
            field=models.TextField(default='This is a test description ;dafofe aijfd;adfoskdf j;osdj'),
            preserve_default=False,
        ),
    ]
