# Generated by Django 5.1.6 on 2025-02-25 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("serve", "0011_alter_messages_table"),
    ]

    operations = [
        migrations.AddField(
            model_name="messages",
            name="time",
            field=models.CharField(default=122220, max_length=32, verbose_name="时间"),
            preserve_default=False,
        ),
    ]
