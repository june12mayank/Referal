# Generated by Django 4.0.2 on 2022-02-10 14:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('company', models.CharField(max_length=30)),
                ('experienceDescription', models.TextField()),
                ('email', models.EmailField(max_length=70)),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=30)),
                ('heading', models.CharField(max_length=70)),
                ('description', models.TextField()),
                ('post_date', models.DateTimeField(verbose_name='Date_Posted')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Referral.person')),
            ],
        ),
    ]
