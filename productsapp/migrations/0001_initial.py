# Generated by Django 2.2.14 on 2020-07-31 09:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('url', models.TextField()),
                ('dop', models.DateTimeField()),
                ('votes_total', models.IntegerField(default=1)),
                ('photo', models.ImageField(upload_to='imagesiam/')),
                ('icon', models.ImageField(upload_to='imagesiam/')),
                ('body', models.TextField()),
                ('hunter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
