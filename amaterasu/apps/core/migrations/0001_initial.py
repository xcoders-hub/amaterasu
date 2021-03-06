# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-03 02:31
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Alias',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.EmailField(max_length=150)),
                ('goto', models.TextField(max_length=150)),
                ('domain', models.CharField(max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now_add=True)),
                ('active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name_plural': 'Aliases',
            },
        ),
        migrations.CreateModel(
            name='ClientProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=15)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['user'],
                'verbose_name': 'Client',
                'verbose_name_plural': 'Clients',
            },
        ),
        migrations.CreateModel(
            name='Domain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('transport', models.CharField(default=b'dovecot', max_length=50)),
                ('have_dns_service', models.BooleanField(default=True)),
                ('active', models.BooleanField(default=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Mailbox',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.EmailField(max_length=150, unique=True)),
                ('password', models.CharField(max_length=250)),
                ('name', models.CharField(max_length=250)),
                ('maildir', models.CharField(blank=True, max_length=150)),
                ('quota', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('local_part', models.CharField(blank=True, max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now_add=True)),
                ('active', models.BooleanField(default=True)),
                ('domain', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Domain')),
            ],
            options={
                'verbose_name_plural': 'Mailboxes',
            },
        ),
        migrations.CreateModel(
            name='PdnsDomains',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('master', models.CharField(blank=True, max_length=128, null=True)),
                ('last_check', models.IntegerField(blank=True, null=True)),
                ('type', models.CharField(max_length=6)),
                ('notified_serial', models.IntegerField(blank=True, null=True)),
                ('account', models.CharField(blank=True, max_length=40, null=True)),
            ],
            options={
                'verbose_name_plural': 'PDNS Domains',
            },
        ),
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('bandwidth', models.DecimalField(decimal_places=2, default=5096, max_digits=10, verbose_name='Bandwidth MB')),
                ('disk_space', models.DecimalField(decimal_places=2, default=300, max_digits=10, verbose_name='Disk Space MB')),
                ('email_accounts', models.IntegerField(default=10)),
                ('ftp_accounts', models.IntegerField(default=5)),
                ('db_mysql', models.IntegerField()),
                ('db_postgres', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('languages', models.ManyToManyField(to='core.Language')),
            ],
        ),
        migrations.CreateModel(
            name='Records',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('type', models.CharField(blank=True, choices=[(b'SOA', b'SOA'), (b'NS', b'NS'), (b'MX', b'MX'), (b'TXT', b'TXT'), (b'PTR', b'PTR'), (b'A', b'A'), (b'AAAA', b'AAAA'), (b'CNAME', b'CNAME')], max_length=10, null=True)),
                ('content', models.CharField(blank=True, max_length=65535, null=True)),
                ('ttl', models.IntegerField(blank=True, null=True)),
                ('prio', models.IntegerField(blank=True, null=True)),
                ('change_date', models.IntegerField(blank=True, null=True)),
                ('domain', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.PdnsDomains')),
            ],
            options={
                'verbose_name_plural': 'Records',
            },
        ),
        migrations.CreateModel(
            name='Supermasters',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.GenericIPAddressField()),
                ('nameserver', models.CharField(max_length=255)),
                ('account', models.CharField(max_length=40)),
            ],
        ),
    ]
