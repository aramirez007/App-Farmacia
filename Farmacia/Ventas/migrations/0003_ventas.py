# Generated by Django 4.2.11 on 2024-05-12 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ventas', '0002_remove_productos_categoria_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ventas',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('fecha', models.DateField()),
                ('usuario', models.CharField(max_length=100)),
                ('total', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
            options={
                'db_table': 'ventas',
                'managed': False,
            },
        ),
    ]
