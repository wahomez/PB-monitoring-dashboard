# Generated by Django 4.1 on 2022-08-25 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateField()),
                ('Open', models.IntegerField()),
                ('High', models.IntegerField()),
                ('Close', models.IntegerField()),
            ],
        ),
    ]
