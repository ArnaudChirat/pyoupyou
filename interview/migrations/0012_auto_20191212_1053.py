# Generated by Django 2.2.5 on 2019-12-12 09:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [("ref", "0002_auto_20190613_1737"), ("interview", "0011_process_other_informations")]

    operations = [
        migrations.CreateModel(
            name="Offer",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=50)),
                ("archived", models.BooleanField(default=False)),
                (
                    "subsidiary",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="ref.Subsidiary", verbose_name="Subsidiary"
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="process",
            name="offer",
            field=models.ForeignKey(
                blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to="interview.Offer"
            ),
        ),
    ]
