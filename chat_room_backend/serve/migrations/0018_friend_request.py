# Generated by Django 5.1.6 on 2025-02-27 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("serve", "0017_group_messages_alter_messages_table"),
    ]

    operations = [
        migrations.CreateModel(
            name="Friend_Request",
            fields=[
                (
                    "time",
                    models.AutoField(
                        primary_key=True, serialize=False, verbose_name="时间"
                    ),
                ),
                ("user1", models.IntegerField(verbose_name="用户1")),
                ("user2", models.IntegerField(verbose_name="用户2")),
            ],
            options={
                "db_table": "Chat_Friend_Request",
            },
        ),
    ]
