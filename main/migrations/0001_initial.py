# Generated by Django 3.2.10 on 2021-12-13 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateTimeField(auto_created=True)),
                ('title', models.CharField(max_length=120)),
                ('link', models.URLField()),
                ('price', models.IntegerField()),
                ('money', models.CharField(choices=[('EUR', 'EUR'), ('USD', 'USD'), ('RUB', 'RUB')], default='EUR', max_length=3)),
            ],
        ),
    ]
