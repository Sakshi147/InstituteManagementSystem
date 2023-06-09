# Generated by Django 4.1.4 on 2023-01-18 04:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('StudentApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Stud_Name', models.CharField(max_length=50)),
                ('Stud_Age', models.IntegerField()),
                ('Stud_Phno', models.BigIntegerField()),
                ('Stud_City', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='StudentApp.city')),
                ('Stud_Course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='StudentApp.course')),
            ],
        ),
    ]
