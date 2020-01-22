# Generated by Django 2.0 on 2020-01-22 11:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('freelance_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='tasks',
        ),
        migrations.AddField(
            model_name='task',
            name='project',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='freelance_app.Project'),
        ),
        migrations.AlterField(
            model_name='project',
            name='deadline',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='deadline',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]