# Generated by Django 2.2.6 on 2019-10-30 07:49

from django.db import migrations, models
import django_resized.forms
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('skillfrontend', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='about',
            options={'verbose_name_plural': 'About Us Management'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Category Management'},
        ),
        migrations.AlterModelOptions(
            name='corevalue',
            options={'verbose_name_plural': 'Core Value Management'},
        ),
        migrations.AlterModelOptions(
            name='enquery',
            options={'verbose_name_plural': 'Enquery Management'},
        ),
        migrations.AlterModelOptions(
            name='ourskill',
            options={'verbose_name_plural': 'Our Skill Management'},
        ),
        migrations.AlterModelOptions(
            name='postdetail',
            options={'verbose_name_plural': 'Post Management'},
        ),
        migrations.AlterModelOptions(
            name='siteaddress',
            options={'verbose_name_plural': 'Address Management'},
        ),
        migrations.AlterModelOptions(
            name='slider',
            options={'verbose_name_plural': 'Slider Management'},
        ),
        migrations.AlterModelOptions(
            name='sociallink',
            options={'verbose_name_plural': 'Social Link Management'},
        ),
        migrations.AlterModelOptions(
            name='whychooseus',
            options={'verbose_name_plural': 'Why Choose Us Management'},
        ),
        migrations.AlterField(
            model_name='about',
            name='content',
            field=tinymce.models.HTMLField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='about',
            name='first_title',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='about',
            name='image1',
            field=django_resized.forms.ResizedImageField(crop=None, force_format=None, keep_meta=True, null=True, quality=0, size=[400, 400], upload_to='about'),
        ),
        migrations.AlterField(
            model_name='about',
            name='image2',
            field=django_resized.forms.ResizedImageField(crop=None, force_format=None, keep_meta=True, null=True, quality=0, size=[400, 400], upload_to='about'),
        ),
        migrations.AlterField(
            model_name='about',
            name='second_title',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='about',
            name='signature',
            field=models.ImageField(null=True, upload_to='about'),
        ),
    ]
