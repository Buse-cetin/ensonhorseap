# Generated by Django 3.2.7 on 2022-08-30 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0007_auto_20220805_1149'),
    ]

    operations = [
        migrations.CreateModel(
            name='Example',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('see', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='message',
            name='date',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='Tarih'),
        ),
    ]
