# Generated by Django 4.1.1 on 2022-10-17 12:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api_portfolio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='media/album/%y/%m/%d')),
            ],
        ),
        migrations.AlterField(
            model_name='audiovisual',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/audiovisual/%y/%m/%d'),
        ),
        migrations.AddField(
            model_name='teatro',
            name='album',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api_portfolio.album'),
        ),
    ]
