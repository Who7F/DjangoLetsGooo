# Generated by Django 4.2.2 on 2023-07-04 18:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('helloworld', '0003_order_rename_peopole_people'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='people',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='helloworld.people'),
        ),
    ]
