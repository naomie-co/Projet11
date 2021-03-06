# Generated by Django 3.0.1 on 2021-03-30 17:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0009_auto_20210310_2333'),
    ]

    operations = [
        migrations.RenameField(
            model_name='store',
            old_name='name',
            new_name='name_store',
        ),
        migrations.AlterField(
            model_name='op_food',
            name='categorie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='search.Categorie'),
        ),
        migrations.RemoveField(
            model_name='op_food',
            name='store_available',
        ),
        migrations.AddField(
            model_name='op_food',
            name='store_available',
            field=models.ManyToManyField(to='search.Store'),
        ),
        migrations.AlterField(
            model_name='substitute',
            name='id_substitute',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='search.Op_food'),
        ),
    ]
