# Generated by Django 4.1.7 on 2023-03-10 20:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_rename_collection_product_collection_id_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='collection_id',
            new_name='collection',
        ),
    ]