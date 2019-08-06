# Generated by Django 2.2.3 on 2019-08-06 22:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sklad', '0007_auto_20190806_2347'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trotuarka',
            name='colorandprice',
        ),
        migrations.RemoveField(
            model_name='zabor',
            name='colorandprice',
        ),
        migrations.AddField(
            model_name='colorandprice',
            name='trotuarka',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='sklad.Trotuarka'),
        ),
    ]