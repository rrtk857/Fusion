# Generated by Django 3.1.5 on 2024-04-12 14:08

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('iwdModuleV2', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Budget',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('budgetIssued', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('quantity', models.IntegerField(default=0)),
                ('cost', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='requests',
            name='billGenerated',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='requests',
            name='billProcessed',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='requests',
            name='billSettled',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='requests',
            name='issuedWorkOrder',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='requests',
            name='workCompleted',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='requests',
            name='deanProcessed',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='requests',
            name='directorApproval',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='requests',
            name='engineerProcessed',
            field=models.IntegerField(default=0),
        ),
        migrations.CreateModel(
            name='WorkOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('date', models.DateField(default=datetime.date.today)),
                ('agency', models.CharField(max_length=200)),
                ('amount', models.IntegerField(default=0)),
                ('deposit', models.IntegerField(default=0)),
                ('alloted_time', models.CharField(max_length=200)),
                ('start_date', models.DateField()),
                ('completion_date', models.DateField()),
                ('request_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='iwdModuleV2.requests')),
            ],
        ),
        migrations.CreateModel(
            name='UsedItems',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('itemName', models.CharField(max_length=200)),
                ('cost', models.IntegerField(default=0)),
                ('quantity', models.IntegerField(default=0)),
                ('date', models.DateField(default=datetime.date.today)),
                ('request_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='iwdModuleV2.requests')),
            ],
        ),
        migrations.CreateModel(
            name='Bills',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='')),
                ('request_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='iwdModuleV2.requests')),
            ],
        ),
    ]
