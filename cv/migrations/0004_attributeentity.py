# Generated by Django 2.1.7 on 2019-03-14 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0003_auto_20190314_1355'),
    ]

    operations = [
        migrations.CreateModel(
            name='AttributeEntity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.TextField()),
                ('value', models.TextField()),
            ],
        ),
    ]