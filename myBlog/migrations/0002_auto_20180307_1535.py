# Generated by Django 2.0.1 on 2018-03-07 07:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myBlog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'verbose_name_plural': '作者'},
        ),
        migrations.AlterModelOptions(
            name='blogbook',
            options={'verbose_name_plural': '博客'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': '分类'},
        ),
        migrations.AlterModelOptions(
            name='tag',
            options={'verbose_name_plural': '标签'},
        ),
    ]
