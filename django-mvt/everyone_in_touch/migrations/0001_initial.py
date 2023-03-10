# Generated by Django 4.1.7 on 2023-03-04 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=128, verbose_name="Teacher's full name")),
                ('bio', models.TextField(max_length=5000, verbose_name="Teacher's bio")),
                ('lesson_price', models.PositiveIntegerField(db_index=True, verbose_name='The price for one lesson')),
                ('language', models.CharField(choices=[('ENG', 'ENGLISH'), ('ES', 'SPANISH'), ('FR', 'FRENCH')], default='ENG', max_length=3)),
            ],
        ),
    ]
