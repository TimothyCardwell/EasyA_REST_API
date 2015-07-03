# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AnswerAttachments',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('attachment', models.FileField(upload_to='answers/%Y/%m/%d')),
                ('date', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='Answers',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('answer', models.TextField()),
                ('date', models.DateTimeField(default=datetime.datetime.now, db_index=True)),
                ('accepted', models.BooleanField()),
            ],
            options={
                'ordering': ['date'],
            },
        ),
        migrations.CreateModel(
            name='Degrees',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Payments',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('fake_column', models.CharField(max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='QuestionAttachments',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('attachment', models.FileField(upload_to='questions/%Y/%m/%d')),
                ('date', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('subject', models.CharField(max_length=100)),
                ('body', models.TextField()),
                ('price', models.DecimalField(max_digits=5, decimal_places=2)),
                ('date', models.DateTimeField(default=datetime.datetime.now, db_index=True)),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
        migrations.CreateModel(
            name='QuestionTags',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('question', models.ForeignKey(to='rest_api.Questions')),
            ],
        ),
        migrations.CreateModel(
            name='Schools',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=15, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserRatings',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('rating', models.IntegerField()),
                ('comment', models.CharField(max_length=255)),
                ('date', models.DateTimeField(default=datetime.datetime.now, db_index=True)),
            ],
            options={
                'ordering': ['date'],
            },
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('first_name', models.CharField(max_length=35)),
                ('last_name', models.CharField(max_length=25)),
                ('email', models.EmailField(max_length=254)),
                ('username', models.CharField(db_index=True, max_length=20)),
                ('password', models.CharField(max_length=30)),
                ('created', models.DateTimeField(default=datetime.datetime.now)),
                ('last_login', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='UserDetails',
            fields=[
                ('users_ptr', models.OneToOneField(primary_key=True, auto_created=True, serialize=False, parent_link=True, to='rest_api.Users')),
                ('age', models.DateField(null=True)),
                ('profession', models.CharField(null=True, max_length=100)),
                ('image', models.ImageField(null=True, upload_to='images/%Y/%m/%d')),
                ('degree', models.OneToOneField(null=True, to='rest_api.Degrees')),
                ('school', models.OneToOneField(null=True, to='rest_api.Schools')),
            ],
            bases=('rest_api.users',),
        ),
        migrations.AddField(
            model_name='userratings',
            name='rater',
            field=models.ForeignKey(related_name='userratings_rater', to='rest_api.Users'),
        ),
        migrations.AddField(
            model_name='userratings',
            name='user',
            field=models.ForeignKey(related_name='userratings_user', to='rest_api.Users'),
        ),
        migrations.AddField(
            model_name='questiontags',
            name='tag',
            field=models.ForeignKey(to='rest_api.Tags'),
        ),
        migrations.AddField(
            model_name='questions',
            name='user',
            field=models.ForeignKey(to='rest_api.Users'),
        ),
        migrations.AddField(
            model_name='questionattachments',
            name='question',
            field=models.ForeignKey(to='rest_api.Questions'),
        ),
        migrations.AddField(
            model_name='answers',
            name='question',
            field=models.ForeignKey(to='rest_api.Questions'),
        ),
        migrations.AddField(
            model_name='answers',
            name='user',
            field=models.ForeignKey(to='rest_api.Users'),
        ),
        migrations.AddField(
            model_name='answerattachments',
            name='answer',
            field=models.ForeignKey(to='rest_api.Answers'),
        ),
    ]
