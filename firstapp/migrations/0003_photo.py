# Generated by Django 3.1.1 on 2020-09-24 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0002_auto_20200925_0049'),
    ]

    operations = [
        migrations.CreateModel(
            name='photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo_num', models.IntegerField(default=0)),
                ('user_id', models.CharField(max_length=255)),
            ],
        ),
    ]
