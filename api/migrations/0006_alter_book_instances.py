# Generated by Django 3.2.4 on 2021-07-15 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_alter_bookinstance_student'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='instances',
            field=models.IntegerField(default=None),
        ),
    ]
