# Generated by Django 2.2 on 2019-12-10 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('sid', models.AutoField(primary_key=True, serialize=False)),
                ('sname', models.CharField(max_length=40)),
                ('sadd', models.CharField(max_length=30)),
            ],
        ),
    ]
