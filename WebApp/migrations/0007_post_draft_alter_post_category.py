# Generated by Django 4.1.1 on 2022-10-26 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("WebApp", "0006_category_post_category"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="draft",
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name="post",
            name="category",
            field=models.CharField(
                choices=[
                    ("Heart Disease", "Heart Disease"),
                    ("Mental Health", "Mental Health"),
                    ("Covid19", "Covid19"),
                    ("Immunization", "Immunization"),
                ],
                max_length=255,
            ),
        ),
    ]