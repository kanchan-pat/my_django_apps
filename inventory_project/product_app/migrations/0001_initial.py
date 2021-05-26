# Generated by Django 3.2.3 on 2021-05-25 21:43

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
                ('name', models.CharField(max_length=30)),
                ('category', models.CharField(choices=[('EL', 'Electronics'), ('FA', 'Fashion'), ('BO', 'Books'), ('CL', 'Cleaning'), ('BE', 'Beauty')], max_length=2)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
            ],
        ),
    ]