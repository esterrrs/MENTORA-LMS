# Generated by Django 5.1.2 on 2024-11-27 03:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_course', models.CharField(max_length=100)),
                ('id_course', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='pengajar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('namaPengajar', models.CharField(max_length=100)),
                ('nidn', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='peserta_didik',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_peserta_didik', models.CharField(max_length=100)),
                ('nim', models.CharField(max_length=20)),
            ],
        ),
    ]