# Generated by Django 3.2.4 on 2021-07-11 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('targetApp', '0029_alter_organization_insert_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization',
            name='domains',
            field=models.ManyToManyField(blank=True, null=True, related_name='domains', to='targetApp.Domain'),
        ),
    ]
