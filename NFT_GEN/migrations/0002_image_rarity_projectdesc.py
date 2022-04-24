# Generated by Django 4.0.2 on 2022-02-04 13:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('NFT_GEN', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='rarity',
            field=models.FloatField(default=0.25),
        ),
        migrations.CreateModel(
            name='ProjectDesc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('proj_name', models.CharField(blank=True, max_length=255, null=True)),
                ('total', models.IntegerField()),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]