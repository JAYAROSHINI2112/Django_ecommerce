# Generated by Django 3.2 on 2023-04-25 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendances', '0005_auto_20230425_0443'),
    ]

    operations = [
        migrations.CreateModel(
            name='fields',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.DeleteModel(
            name='selectfields',
        ),
    ]
