# Generated by Django 3.2.9 on 2022-01-15 15:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profession',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, verbose_name='Наименование')),
            ],
        ),
        migrations.CreateModel(
            name='SkillOfWarrior',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.IntegerField(verbose_name='Уровень освоения умения')),
                ('skill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='worriors_app.skill', verbose_name='Умение')),
            ],
        ),
        migrations.CreateModel(
            name='Worrior',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('race', models.CharField(choices=[('s', 'student'), ('t', 'teamlead'), ('d', 'developer')], max_length=1, verbose_name='Раса')),
                ('name', models.CharField(max_length=120, verbose_name='Имя')),
                ('level', models.IntegerField(default=0, verbose_name='Уровень')),
                ('profession', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='worriors_app.profession', verbose_name='Профессия')),
                ('skill', models.ManyToManyField(related_name='worrior_skills', through='worriors_app.SkillOfWarrior', to='worriors_app.Skill', verbose_name='Умения')),
            ],
        ),
        migrations.AddField(
            model_name='skillofwarrior',
            name='worrior',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='worriors_app.worrior', verbose_name='Воин'),
        ),
    ]