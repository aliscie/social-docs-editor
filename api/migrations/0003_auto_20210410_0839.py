# Generated by Django 3.1.3 on 2021-04-10 08:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20210410_0825'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='preBuildStyle',
            new_name='pre_build_style',
        ),
        migrations.AlterField(
            model_name='comment',
            name='the_post',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='comment', to='api.post'),
        ),
    ]
