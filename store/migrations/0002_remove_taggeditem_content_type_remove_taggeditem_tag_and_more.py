# Generated by Django 4.1.7 on 2023-03-08 23:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="taggeditem",
            name="content_type",
        ),
        migrations.RemoveField(
            model_name="taggeditem",
            name="tag",
        ),
        migrations.DeleteModel(
            name="Tag",
        ),
        migrations.DeleteModel(
            name="TaggedItem",
        ),
    ]