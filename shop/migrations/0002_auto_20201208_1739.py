# Generated by Django 3.1.4 on 2020-12-08 17:39

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=250, unique=True)),
                ('description', models.TextField(blank=True)),
                ('image', models.ImageField(blank=True, upload_to='category')),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
                'ordering': ('name',),
            },
        ),
        migrations.AlterModelOptions(
            name='item',
            options={'ordering': ('title',), 'verbose_name': 'item', 'verbose_name_plural': 'items'},
        ),
        migrations.AddField(
            model_name='item',
            name='avaliable',
            field=models.BooleanField(default=True, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='stock',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.category'),
        ),
    ]
