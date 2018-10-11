# Generated by Django 2.1.2 on 2018-10-11 14:54

import contratospr.contracts.models
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django_s3_storage.storage


class Migration(migrations.Migration):

    dependencies = [
        ('contracts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='preview_data',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='document',
            name='file',
            field=models.FileField(blank=True, null=True, storage=django_s3_storage.storage.S3Storage(), upload_to=contratospr.contracts.models.document_file_path),
        ),
    ]