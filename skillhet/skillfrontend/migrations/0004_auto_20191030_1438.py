# Generated by Django 2.2.6 on 2019-10-30 09:08

from django.db import migrations, models
import django_resized.forms
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('skillfrontend', '0003_auto_20191030_1322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enquery',
            name='email',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='enquery',
            name='message',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='enquery',
            name='mobile',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='enquery',
            name='name',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='enquery',
            name='subject',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='ourskill',
            name='content1',
            field=models.TextField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='ourskill',
            name='content2',
            field=models.TextField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='ourskill',
            name='content3',
            field=models.TextField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='ourskill',
            name='heading',
            field=models.CharField(default=None, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='ourskill',
            name='image',
            field=django_resized.forms.ResizedImageField(crop=None, default=None, force_format=None, keep_meta=True, null=True, quality=0, size=[750, 750], upload_to='our_skill'),
        ),
        migrations.AlterField(
            model_name='ourskill',
            name='title1',
            field=models.CharField(default=None, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='ourskill',
            name='title2',
            field=models.CharField(default=None, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='ourskill',
            name='title3',
            field=models.CharField(default=None, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='postdetail',
            name='content1',
            field=tinymce.models.HTMLField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='postdetail',
            name='content2',
            field=tinymce.models.HTMLField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='postdetail',
            name='image1',
            field=django_resized.forms.ResizedImageField(crop=None, default=None, force_format=None, keep_meta=True, null=True, quality=0, size=[456, 286], upload_to='post_details'),
        ),
        migrations.AlterField(
            model_name='postdetail',
            name='image2',
            field=django_resized.forms.ResizedImageField(crop=None, default=None, force_format=None, keep_meta=True, null=True, quality=0, size=[456, 303], upload_to='post_details'),
        ),
        migrations.AlterField(
            model_name='postdetail',
            name='main_content',
            field=tinymce.models.HTMLField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='postdetail',
            name='slider_image1',
            field=django_resized.forms.ResizedImageField(crop=None, default=None, force_format=None, keep_meta=True, null=True, quality=0, size=[1000, 500], upload_to='post_details'),
        ),
        migrations.AlterField(
            model_name='postdetail',
            name='slider_image2',
            field=django_resized.forms.ResizedImageField(crop=None, default=None, force_format=None, keep_meta=True, null=True, quality=0, size=[1000, 500], upload_to='post_details'),
        ),
        migrations.AlterField(
            model_name='postdetail',
            name='slider_image3',
            field=django_resized.forms.ResizedImageField(crop=None, default=None, force_format=None, keep_meta=True, null=True, quality=0, size=[1000, 500], upload_to='post_details'),
        ),
        migrations.AlterField(
            model_name='postdetail',
            name='sub_title1',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='postdetail',
            name='sub_title2',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='postdetail',
            name='sub_title3',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='postdetail',
            name='title1',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='postdetail',
            name='title2',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
