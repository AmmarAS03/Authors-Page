# Generated by Django 4.1 on 2022-11-10 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0003_alter_authors_organization'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authors',
            name='country',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='authors',
            name='first_name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='authors',
            name='last_name',
            field=models.CharField(max_length=50),
        ),
    ]