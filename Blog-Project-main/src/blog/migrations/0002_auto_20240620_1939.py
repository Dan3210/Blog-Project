# Generated by Django 3.2.9 on 2024-06-20 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('e', 'Entertainment'), ('m', 'Music'), ('i', 'IT')], default='e', max_length=15),
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
