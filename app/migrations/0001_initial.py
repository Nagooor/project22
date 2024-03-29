# Generated by Django 4.2.6 on 2023-12-11 10:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bonus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('deptno', models.IntegerField(primary_key=True, serialize=False)),
                ('dname', models.CharField(max_length=100, unique=True)),
                ('loc', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Salgrade',
            fields=[
                ('grade', models.IntegerField(primary_key=True, serialize=False)),
                ('losal', models.IntegerField()),
                ('hisal', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('empno', models.IntegerField(primary_key=True, serialize=False)),
                ('ename', models.CharField(max_length=100)),
                ('job', models.CharField(max_length=100)),
                ('mgr', models.IntegerField()),
                ('hiredate', models.DateField()),
                ('sal', models.IntegerField()),
                ('comm', models.IntegerField()),
                ('deptno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.department')),
            ],
        ),
    ]
