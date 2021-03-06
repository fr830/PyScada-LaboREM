# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-06-21 12:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pyscada', '0042_auto_20180604_1240'),
    ]

    operations = [
        migrations.CreateModel(
            name='LaboremMotherboardDevice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='LaboremMotherboardIOConfig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=255)),
                ('description', models.TextField(default='', null=True, verbose_name='Description')),
            ],
        ),
        migrations.CreateModel(
            name='LaboremMotherboardIOElement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=255)),
                ('description', models.TextField(default='', null=True, verbose_name='Description')),
            ],
        ),
        migrations.CreateModel(
            name='LaboremMotherboardVariable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plug', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'), ('11', '11'), ('12', '12'), ('13', '13'), ('14', '14'), ('15', '15'), ('16', '16')], max_length=254)),
                ('laboremmotherboard_variable', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pyscada.Variable')),
            ],
        ),
        migrations.CreateModel(
            name='LaboremPlugDevice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=255)),
                ('description', models.TextField(default='', null=True, verbose_name='Description')),
                ('plug_image', models.ImageField(blank=True, upload_to='img/laborem/plugs/', verbose_name='plug image')),
                ('level', models.CharField(choices=[('1', 'Easy'), ('2', 'Medium'), ('3', 'Hard')], max_length=254)),
                ('motherboardIOConfig', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='laborem.LaboremMotherboardIOConfig')),
            ],
        ),
        migrations.AddField(
            model_name='laboremmotherboardioconfig',
            name='C0',
            field=models.ForeignKey(help_text='C0 connector', on_delete=django.db.models.deletion.CASCADE, related_name='mobo_C0', to='laborem.LaboremMotherboardIOElement'),
        ),
        migrations.AddField(
            model_name='laboremmotherboardioconfig',
            name='C1',
            field=models.ForeignKey(help_text='C1 connector', on_delete=django.db.models.deletion.CASCADE, related_name='mobo_C1', to='laborem.LaboremMotherboardIOElement'),
        ),
        migrations.AddField(
            model_name='laboremmotherboardioconfig',
            name='C2',
            field=models.ForeignKey(help_text='C2 connector', on_delete=django.db.models.deletion.CASCADE, related_name='mobo_C2', to='laborem.LaboremMotherboardIOElement'),
        ),
        migrations.AddField(
            model_name='laboremmotherboardioconfig',
            name='C3',
            field=models.ForeignKey(help_text='C3 connector', on_delete=django.db.models.deletion.CASCADE, related_name='mobo_C3', to='laborem.LaboremMotherboardIOElement'),
        ),
        migrations.AddField(
            model_name='laboremmotherboardioconfig',
            name='C4',
            field=models.ForeignKey(help_text='C4 connector', on_delete=django.db.models.deletion.CASCADE, related_name='mobo_C4', to='laborem.LaboremMotherboardIOElement'),
        ),
        migrations.AddField(
            model_name='laboremmotherboardioconfig',
            name='C5',
            field=models.ForeignKey(help_text='C5 connector', on_delete=django.db.models.deletion.CASCADE, related_name='mobo_C5', to='laborem.LaboremMotherboardIOElement'),
        ),
        migrations.AddField(
            model_name='laboremmotherboardioconfig',
            name='C6',
            field=models.ForeignKey(help_text='C6 connector', on_delete=django.db.models.deletion.CASCADE, related_name='mobo_C6', to='laborem.LaboremMotherboardIOElement'),
        ),
        migrations.AddField(
            model_name='laboremmotherboardioconfig',
            name='C7',
            field=models.ForeignKey(help_text='C7 connector', on_delete=django.db.models.deletion.CASCADE, related_name='mobo_C7', to='laborem.LaboremMotherboardIOElement'),
        ),
        migrations.AddField(
            model_name='laboremmotherboardioconfig',
            name='V0',
            field=models.ForeignKey(help_text='V0 connector', on_delete=django.db.models.deletion.CASCADE, related_name='mobo_V0', to='laborem.LaboremMotherboardIOElement'),
        ),
        migrations.AddField(
            model_name='laboremmotherboardioconfig',
            name='V1',
            field=models.ForeignKey(help_text='V1 connector', on_delete=django.db.models.deletion.CASCADE, related_name='mobo_V1', to='laborem.LaboremMotherboardIOElement'),
        ),
        migrations.AddField(
            model_name='laboremmotherboardioconfig',
            name='V2',
            field=models.ForeignKey(help_text='V2 connector', on_delete=django.db.models.deletion.CASCADE, related_name='mobo_V2', to='laborem.LaboremMotherboardIOElement'),
        ),
        migrations.AddField(
            model_name='laboremmotherboardioconfig',
            name='V3',
            field=models.ForeignKey(help_text='V3 connector', on_delete=django.db.models.deletion.CASCADE, related_name='mobo_V3', to='laborem.LaboremMotherboardIOElement'),
        ),
        migrations.AddField(
            model_name='laboremmotherboardioconfig',
            name='pinA',
            field=models.ForeignKey(help_text='Relay', on_delete=django.db.models.deletion.CASCADE, related_name='mobo_pinA', to='laborem.LaboremMotherboardIOElement'),
        ),
        migrations.AddField(
            model_name='laboremmotherboardioconfig',
            name='pinB',
            field=models.ForeignKey(help_text='A0 connector', on_delete=django.db.models.deletion.CASCADE, related_name='mobo_pinB', to='laborem.LaboremMotherboardIOElement'),
        ),
        migrations.AddField(
            model_name='laboremmotherboardioconfig',
            name='pinC',
            field=models.ForeignKey(help_text='A1 connector', on_delete=django.db.models.deletion.CASCADE, related_name='mobo_pinC', to='laborem.LaboremMotherboardIOElement'),
        ),
        migrations.AddField(
            model_name='laboremmotherboardioconfig',
            name='pinD',
            field=models.ForeignKey(help_text='A2 connector', on_delete=django.db.models.deletion.CASCADE, related_name='mobo_pinD', to='laborem.LaboremMotherboardIOElement'),
        ),
        migrations.AddField(
            model_name='laboremmotherboardioconfig',
            name='pinE',
            field=models.ForeignKey(help_text='A3 connector', on_delete=django.db.models.deletion.CASCADE, related_name='mobo_pinE', to='laborem.LaboremMotherboardIOElement'),
        ),
        migrations.AddField(
            model_name='laboremmotherboarddevice',
            name='MotherboardIOConfig',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='laborem.LaboremMotherboardIOConfig'),
        ),
        migrations.AddField(
            model_name='laboremmotherboarddevice',
            name='laboremmotherboard_device',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pyscada.Device'),
        ),
        migrations.AddField(
            model_name='laboremmotherboarddevice',
            name='plug1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mobo_plug1', to='laborem.LaboremPlugDevice'),
        ),
        migrations.AddField(
            model_name='laboremmotherboarddevice',
            name='plug10',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mobo_plug10', to='laborem.LaboremPlugDevice'),
        ),
        migrations.AddField(
            model_name='laboremmotherboarddevice',
            name='plug11',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mobo_plug11', to='laborem.LaboremPlugDevice'),
        ),
        migrations.AddField(
            model_name='laboremmotherboarddevice',
            name='plug12',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mobo_plug12', to='laborem.LaboremPlugDevice'),
        ),
        migrations.AddField(
            model_name='laboremmotherboarddevice',
            name='plug13',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mobo_plug13', to='laborem.LaboremPlugDevice'),
        ),
        migrations.AddField(
            model_name='laboremmotherboarddevice',
            name='plug14',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mobo_plug14', to='laborem.LaboremPlugDevice'),
        ),
        migrations.AddField(
            model_name='laboremmotherboarddevice',
            name='plug15',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mobo_plug15', to='laborem.LaboremPlugDevice'),
        ),
        migrations.AddField(
            model_name='laboremmotherboarddevice',
            name='plug16',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mobo_plug16', to='laborem.LaboremPlugDevice'),
        ),
        migrations.AddField(
            model_name='laboremmotherboarddevice',
            name='plug2',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mobo_plug2', to='laborem.LaboremPlugDevice'),
        ),
        migrations.AddField(
            model_name='laboremmotherboarddevice',
            name='plug3',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mobo_plug3', to='laborem.LaboremPlugDevice'),
        ),
        migrations.AddField(
            model_name='laboremmotherboarddevice',
            name='plug4',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mobo_plug4', to='laborem.LaboremPlugDevice'),
        ),
        migrations.AddField(
            model_name='laboremmotherboarddevice',
            name='plug5',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mobo_plug5', to='laborem.LaboremPlugDevice'),
        ),
        migrations.AddField(
            model_name='laboremmotherboarddevice',
            name='plug6',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mobo_plug6', to='laborem.LaboremPlugDevice'),
        ),
        migrations.AddField(
            model_name='laboremmotherboarddevice',
            name='plug7',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mobo_plug7', to='laborem.LaboremPlugDevice'),
        ),
        migrations.AddField(
            model_name='laboremmotherboarddevice',
            name='plug8',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mobo_plug8', to='laborem.LaboremPlugDevice'),
        ),
        migrations.AddField(
            model_name='laboremmotherboarddevice',
            name='plug9',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mobo_plug9', to='laborem.LaboremPlugDevice'),
        ),
    ]
