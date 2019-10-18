# Generated by Django 2.2.5 on 2019-10-18 13:37

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [("interview", "0009_auto_20190613_1737")]

    operations = [
        migrations.AddField(
            model_name="process",
            name="last_state_change",
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name="Last State Change"),
        ),
        migrations.AlterField(
            model_name="interview",
            name="state",
            field=models.CharField(
                choices=[
                    ("NP", "NEED PLANIFICATION"),
                    ("PR", "WAIT PLANIFICATION RESPONSE"),
                    ("PL", "PLANNED"),
                    ("GO", "GO"),
                    ("NO", "NO"),
                    ("DR", "DRAFT"),
                    ("WI", "WAIT INFORMATION"),
                ],
                max_length=3,
                verbose_name="next state",
            ),
        ),
        migrations.AlterField(
            model_name="process",
            name="state",
            field=models.CharField(
                choices=[
                    ("OP", "Open"),
                    ("WA", "Waiting interviewer to be designed"),
                    ("WK", "Waiting next interview designation or process termination"),
                    ("JO", "Waiting candidate feedback after a job offer"),
                    ("WP", "Waiting interview planification"),
                    ("WR", "Waiting for interview planification response"),
                    ("WM", "Waiting interview minute"),
                    ("WI", "Waiting interview"),
                    ("NG", "Last interviewer interupt process"),
                    ("CD", "Candidate declined our offer"),
                    ("HI", "Candidate accepted our offer"),
                    ("NO", "Closed - other reason"),
                ],
                default="WA",
                max_length=3,
                verbose_name="Closed reason",
            ),
        ),
    ]
