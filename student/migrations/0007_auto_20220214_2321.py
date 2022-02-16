# Generated by Django 3.0.5 on 2022-02-14 17:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0006_auto_20220207_1900'),
    ]

    operations = [
        migrations.CreateModel(
            name='Centre',
            fields=[
                ('id', models.CharField(max_length=2000, primary_key=True, serialize=False, unique=True)),
                ('centre_name', models.CharField(max_length=2000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.CharField(max_length=2000, primary_key=True, serialize=False, unique=True)),
                ('professor_name', models.CharField(max_length=2000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.CharField(max_length=2000, primary_key=True, serialize=False, unique=True)),
                ('program_name', models.CharField(max_length=2000, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='activity',
            name='centre',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='student.Centre'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='activity',
            name='professor',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='student.Professor'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='activity',
            name='program',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='student.Program'),
            preserve_default=False,
        ),
    ]
