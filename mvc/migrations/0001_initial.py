# Generated by Django 2.1.3 on 2018-12-20 06:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='地名')),
                ('code', models.CharField(max_length=255, verbose_name='代码')),
                ('type', models.IntegerField(choices=[(0, '国家'), (1, '省'), (2, '市'), (3, '区县')], verbose_name='类型')),
                ('parent', models.IntegerField(verbose_name='父级编号(关联自已)')),
            ],
            options={
                'verbose_name': '所在地',
                'verbose_name_plural': '所在地',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='名称')),
            ],
            options={
                'verbose_name': '分类',
                'verbose_name_plural': '分类',
            },
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('message', models.TextField(verbose_name='消息')),
                ('addtime', models.DateTimeField(auto_now=True, verbose_name='发布时间')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mvc.Category', verbose_name='来源')),
            ],
            options={
                'verbose_name': '消息',
                'verbose_name_plural': '消息',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=20, verbose_name='用户名')),
                ('password', models.CharField(max_length=100, verbose_name='密码')),
                ('realname', models.CharField(max_length=20, verbose_name='姓名')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('face', models.ImageField(blank=True, default='', upload_to='face/%Y/%m/%d', verbose_name='头像')),
                ('url', models.CharField(blank=True, default='', max_length=200, verbose_name='个人主页')),
                ('about', models.TextField(blank=True, default='', max_length=1000, verbose_name='关于我')),
                ('addtime', models.DateTimeField(auto_now=True, verbose_name='注册时间')),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mvc.Area', verbose_name='地区')),
                ('friend', models.ManyToManyField(related_name='_user_friend_+', to='mvc.User', verbose_name='朋友')),
            ],
            options={
                'verbose_name': '用户',
                'verbose_name_plural': '用户',
            },
        ),
        migrations.AddField(
            model_name='note',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mvc.User', verbose_name='发布者'),
        ),
    ]
