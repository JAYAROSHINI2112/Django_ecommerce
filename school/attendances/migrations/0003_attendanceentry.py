# Generated by Django 3.2 on 2023-04-24 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendances', '0002_alter_attendclassmaster_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='attendanceentry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('studid', models.IntegerField()),
                ('classid', models.IntegerField()),
                ('dateid', models.IntegerField()),
                ('pafield', models.BooleanField()),
            ],
        ),
    ]
