# Generated by Django 4.2.1 on 2023-05-31 15:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vier_node', '0002_pricing_table_created_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pricing_table',
            name='created_at',
        ),
    ]
