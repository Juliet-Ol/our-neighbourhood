# Generated by Django 4.0.4 on 2022-04-17 15:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('neighbourhoodwatch', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='neighbourhood',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='neighbourhoodwatch.neighbourhood'),
        ),
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('business_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('neighbourhood', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='neighbourhoodwatch.neighbourhood')),
                ('user', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
