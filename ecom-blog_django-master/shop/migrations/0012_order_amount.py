# Generated by Django 4.2.3 on 2023-07-27 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0011_alter_contact_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='amount',
            field=models.IntegerField(default=0, max_length=100),
        ),
    ]