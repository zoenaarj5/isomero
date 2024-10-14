# Generated by Django 5.1.1 on 2024-10-14 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Umusomyi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=130)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('birth_date', models.DateField(null=True)),
                ('sex', models.CharField(choices=[('M', 'Gabo'), ('F', 'Gore')], default=None, max_length=1)),
            ],
        ),
    ]