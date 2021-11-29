# Generated by Django 3.2.4 on 2021-10-07 01:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chef',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('title', models.CharField(max_length=30)),
                ('bio', models.TextField()),
                ('image', models.ImageField(upload_to='chef/')),
            ],
            options={
                'verbose_name': 'chef',
                'verbose_name_plural': 'chefs',
            },
        ),
        migrations.CreateModel(
            name='WhyChooseUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('content', models.TextField()),
            ],
            options={
                'verbose_name': 'why choose us',
                'verbose_name_plural': 'why choose us',
            },
        ),
    ]