# Generated by Django 4.0.2 on 2022-02-26 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xit', '0006_partner_image_hover'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('dept', models.CharField(max_length=50)),
            ],
        ),
    ]
