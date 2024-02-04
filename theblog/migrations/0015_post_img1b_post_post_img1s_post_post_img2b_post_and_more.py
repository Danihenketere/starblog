# Generated by Django 5.0.1 on 2024-02-04 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0014_post_advert_alter_post_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='img1b_post',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='img1s_post',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='img2b_post',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='img2s_post',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='img3b_post',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='img3s_post',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='aboutus',
            name='body',
            field=models.TextField(default='That is'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='category',
            name='body',
            field=models.TextField(default='That is'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='category',
            name='snippet',
            field=models.CharField(default='Click Link Above To Lead Blog Post...', max_length=255),
        ),
        migrations.AlterField(
            model_name='contactus',
            name='body',
            field=models.TextField(default='That is it'),
            preserve_default=False,
        ),
    ]