# Generated by Django 4.2.3 on 2023-07-15 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='produto',
            old_name='id_produto',
            new_name='id',
        ),
        migrations.RemoveField(
            model_name='produto',
            name='descricao',
        ),
        migrations.RemoveField(
            model_name='produto',
            name='nome',
        ),
        migrations.RemoveField(
            model_name='produto',
            name='preco',
        ),
        migrations.AddField(
            model_name='produto',
            name='description',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='produto',
            name='name',
            field=models.CharField(default='', max_length=255, verbose_name='Nome Produto'),
        ),
        migrations.AddField(
            model_name='produto',
            name='price',
            field=models.FloatField(default=0.0),
        ),
    ]