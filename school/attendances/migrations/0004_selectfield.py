# Generated by Django 3.2 on 2023-04-25 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendances', '0003_attendanceentry'),
    ]

    operations = [
        migrations.CreateModel(
            name='selectfield',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
    ]
