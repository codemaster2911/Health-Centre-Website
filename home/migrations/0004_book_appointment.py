# Generated by Django 3.2.3 on 2021-06-27 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_patient'),
    ]

    operations = [
        migrations.CreateModel(
            name='book_appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=30)),
                ('lname', models.CharField(max_length=30)),
                ('phone', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=30)),
                ('dob', models.CharField(max_length=30)),
                ('gender', models.CharField(max_length=30)),
                ('desc', models.CharField(max_length=30)),
            ],
        ),
    ]