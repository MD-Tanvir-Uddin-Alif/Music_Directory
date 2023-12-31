# Generated by Django 4.2.7 on 2023-12-06 18:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('musician', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Album_Name', models.CharField(max_length=100)),
                ('Album_Release_Date', models.DateField()),
                ('Rating', models.ImageField(upload_to='')),
                ('Musician', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='musician.musician')),
            ],
        ),
    ]
