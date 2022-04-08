# Generated by Django 3.2.7 on 2022-03-06 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='Название новости')),
                ('content', models.TextField(blank=True, verbose_name='Контент новости')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания новости')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата обновления новости')),
                ('photo', models.ImageField(upload_to='photos/%Y/%m/%d', verbose_name='Фото новости')),
                ('is_published', models.BooleanField(default=True, verbose_name='Опубликовано?')),
            ],
            options={
                'verbose_name': 'Новость',
                'verbose_name_plural': 'Новости',
            },
        ),
    ]
