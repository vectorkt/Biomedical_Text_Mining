# Generated by Django 3.0.5 on 2020-05-12 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ppi', '0002_proteinstocheck'),
    ]

    operations = [
        migrations.CreateModel(
            name='ToCheck',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.RenameModel(
            old_name='ProteinsToCheck',
            new_name='CurrentCheckList',
        ),
    ]
