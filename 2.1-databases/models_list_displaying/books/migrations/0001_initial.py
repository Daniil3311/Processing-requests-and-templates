# Generated by Django 4.1.7 on 2023-03-12 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='Название')),
                ('author', models.CharField(max_length=64, verbose_name='Автор')),
                ('pub_date', models.DateField(verbose_name='Дата публикации')),
            ],
        ),
    ]