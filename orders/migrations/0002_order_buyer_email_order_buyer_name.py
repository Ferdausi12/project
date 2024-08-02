# Generated by Django 4.2.3 on 2024-07-17 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='buyer_email',
            field=models.EmailField(default='default@example.com', max_length=254),
        ),
        migrations.AddField(
            model_name='order',
            name='buyer_name',
            field=models.CharField(default='Unknown', max_length=100),
            preserve_default=False,
        ),
    ]
