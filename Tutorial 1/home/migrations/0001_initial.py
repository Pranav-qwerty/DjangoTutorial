# Generated by Django 3.1.3 on 2020-12-07 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=122)),
                ('passward', models.CharField(max_length=50)),
                ('Address', models.CharField(max_length=300)),
                ('Address2', models.CharField(max_length=300)),
                ('City', models.CharField(max_length=100)),
                ('State', models.CharField(max_length=50)),
                ('Zip_Code', models.CharField(max_length=5)),
                ('Cheak_me_out', models.CharField(max_length=10)),
            ],
        ),
    ]