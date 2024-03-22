# Generated by Django 4.2.11 on 2024-03-22 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('rollno', models.CharField(max_length=20)),
                ('year', models.IntegerField(choices=[(1, 'First Year'), (2, 'Second Year'), (3, 'Third Year'), (4, 'Fourth Year')])),
                ('event_type', models.CharField(choices=[('national', 'National'), ('state', 'State'), ('district', 'District')], max_length=20)),
                ('intercollege_mcq', models.BooleanField(default=False)),
                ('intracollege_mcq', models.BooleanField(default=False)),
                ('position', models.CharField(choices=[('1st', '1st'), ('2nd', '2nd'), ('3rd', '3rd'), ('none', 'None')], max_length=10)),
            ],
        ),
    ]